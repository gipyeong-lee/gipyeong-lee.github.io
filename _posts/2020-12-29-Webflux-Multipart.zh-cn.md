---
layout: post
title: "Webflux - 使用 multipart 上传文件"
tags: [multipart, upload]
style: border
color: danger
description: Webflux multipart 上传示例。
lang: zh-cn
ref: 2020-12-29-Webflux-Multipart
---


## 阅读本文后你将了解到什么？

如何在 Webflux 服务器上上传文件以及如何进行处理。

我在下面编写了非常简单的代码，按照这些代码操作后，你就可以处理多文件上传及其他相关操作。

## 代码

```kotlin
fun uploadImage(serverRequest: ServerRequest): Mono<ServerResponse> {
    val monos = serverRequest.multipartData().flatMap { multipart ->
        // 1. 获取 multipart 文件
        val files = multipart["file"] ?: listOf()
        // 2. 创建 mono 发布者，因为此代码位于 flatMap 中
        return @flatMap Mono.just(files.map { part ->
            val filePart = part.cast<FilePart>()
            // 3. 从 Flux<DataBuffer> 读取 DataBuffer，并使用 SequenceInputStream 通过 reduce 转换为 Mono
            filePart.content().reduce(object : InputStream() {
                override fun read() = -1
            }) { s: InputStream, d -> SequenceInputStream(s, d.asInputStream(true)) }
                    .flatMap { inputStream ->
                    // 4. 完成从 flux 读取 inputStream 后，读取 inputStream 的字节。（** 注意：调用 readBytes 函数后会关闭流，因此无法重复使用 inputStream）
                        val bytes = inputStream.readBytes() 

                        // 5. 现在你可以随意使用这些字节。在本例中，我将文件包装在 Mono 中上传到 S3 存储桶。

                        return @flatMap Mono.just(s3Uploader.upload(filePart.filename(), filePart.headers().contentType.toString(), ByteArrayInputStream(bytes), bytes.size.toLong()))
                    }
        })
    }
    return monos.flatMap { responses ->
        // 6. 使用 `Mono.zip` 在所有文件上传完成后进行响应。
        Mono.zip(responses, this::resultWithUpload).flatMap {
            // 7. 在所有文件上传到 S3 后，我向客户端返回响应。
            ServerResponse.ok().body(BodyInserters.fromValue(it))
        }
    }
}

fun resultWithUpload(results: Array<Any>): List<s3UploadResponse> {
    return results.map { return @map it as s3UploadResponse }.toList()
}
```

## 结论

一个非常简单的上传示例。现在你可以使用 Webflux 技术栈来处理文件了。

> _求知若渴，虚心若愚_
