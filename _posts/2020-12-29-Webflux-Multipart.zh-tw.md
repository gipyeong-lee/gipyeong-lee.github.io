---
layout: post
title: "Webflux - 使用 multipart 上傳檔案"
tags: [multipart, upload]
style: border
color: danger
description: Webflux 上傳 multipart 範例。
lang: zh-tw
ref: 2020-12-29-Webflux-Multipart
---


## 閱讀本文後，您將了解到？

如何在 Webflux 伺服器上上傳檔案以及如何處理它。

我在下方編寫了非常簡單的程式碼，只要跟隨這些程式碼，您就能處理多個檔案上傳以及其他相關操作。

## 程式碼

```kotlin
fun uploadImage(serverRequest: ServerRequest): Mono<ServerResponse> {
    val monos = serverRequest.multipartData().flatMap { multipart ->
        // 1. 獲取 multipart 檔案
        val files = multipart["file"] ?: listOf()
        // 2. 建立 mono publisher，因為我們在 flatMap 下編寫此程式碼
        return @flatMap Mono.just(files.map { part ->
            val filePart = part.cast<FilePart>()
            // 3. 從 Flux<DataBuffer> 讀取 `DataBuffer`，並使用 SequenceInputStream 透過 reduce 轉換為 Mono
            filePart.content().reduce(object : InputStream() {
                override fun read() = -1
            }) { s: InputStream, d -> SequenceInputStream(s, d.asInputStream(true)) }
                    .flatMap { inputStream ->
                    // 4. 完成從 flux 讀取 inputStream 後，讀取 inputStream 的位元組。（** 執行 readBytes 函數後將關閉您的串流，因此您無法重複使用 inputStream）
                        val bytes = inputStream.readBytes() 

                        // 5. 現在您可以隨意使用這些位元組。在此範例中，我將檔案封裝在 Mono 中並上傳到 S3 儲存桶。

                        return @flatMap Mono.just(s3Uploader.upload(filePart.filename(), filePart.headers().contentType.toString(), ByteArrayInputStream(bytes), bytes.size.toLong()))
                    }
        })
    }
    return monos.flatMap { responses ->
        // 6. 在所有檔案上傳後，使用 `Mono zip` 進行回應。
        Mono.zip(responses, this::resultWithUpload).flatMap {
            // 7. 所有檔案上傳至 S3 後，我向用戶端做出回應。
            ServerResponse.ok().body(BodyInserters.fromValue(it))
        }
    }
}

fun resultWithUpload(results: Array<Any>): List<s3UploadResponse> {
    return results.map { return @map it as s3UploadResponse }.toList()
}
```

## 總結

非常簡單的上傳範例。現在您可以使用 Webflux 技術棧處理檔案了。

> _Stay Hunger, Stay Foolish_
