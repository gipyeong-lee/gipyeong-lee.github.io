---
layout: post
title: "Webflux - マルチパートでのファイルアップロード"
tags: [multipart, upload]
style: border
color: danger
description: Webfluxのマルチパートアップロードの例。
lang: ja
ref: 2020-12-29-Webflux-Multipart
---


## この記事を読むとわかること

Webfluxサーバー上でのファイルアップロードとその処理方法について解説します。

以下に非常にシンプルなコードを記述しました。このコードに従えば、他の処理を行いながら複数のアップロードファイルを扱うことができます。

## コード

```kotlin
fun uploadImage(serverRequest: ServerRequest): Mono<ServerResponse> {
    val monos = serverRequest.multipartData().flatMap { multipart ->
        // 1. マルチパートファイルを取得
        val files = multipart["file"] ?: listOf()
        // 2. Monoパブリッシャーを作成（flatMap内で記述しているため）
        return @flatMap Mono.just(files.map { part ->
            val filePart = part.cast<FilePart>()
            // 3. Flux<DataBuffer>からDataBufferを読み込み、SequenceInputStreamを使用してreduceでMonoに変換
            filePart.content().reduce(object : InputStream() {
                override fun read() = -1
            }) { s: InputStream, d -> SequenceInputStream(s, d.asInputStream(true)) }
                    .flatMap { inputStream ->
                    // 4. FluxからInputStreamの読み込みが完了した後、InputStreamのバイト列を読み込む（** readBytes関数を実行するとストリームが閉じられるため、InputStreamは再利用できません）
                        val bytes = inputStream.readBytes() 

                        // 5. これでバイト列を自由に使用できます。この例では、MonoでラップしてファイルをS3バケットにアップロードしています。

                        return @flatMap Mono.just(s3Uploader.upload(filePart.filename(), filePart.headers().contentType.toString(), ByteArrayInputStream(bytes), bytes.size.toLong()))
                    }
        })
    }
    return monos.flatMap { responses ->
        // 6. すべてのファイルがアップロードされた後に応答するために Mono.zip を使用
        Mono.zip(responses, this::resultWithUpload).flatMap {
            // 7. すべてのファイルがS3にアップロードされた後、クライアントに応答
            ServerResponse.ok().body(BodyInserters.fromValue(it))
        }
    }
}

fun resultWithUpload(results: Array<Any>): List<s3UploadResponse> {
    return results.map { return @map it as s3UploadResponse }.toList()
}
```

## 結論

非常にシンプルなアップロードの例でした。これでWebfluxスタックでファイルを扱えるようになります。

> _ハングリーであれ。愚か者であれ。_
