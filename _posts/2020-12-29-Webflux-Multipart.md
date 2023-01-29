---
layout: post
title: "Webflux - Upload files with multipart"
tags: [multipart, upload]
style: border
color: danger
description: Webflux upload multipart example.
---


## What you can know after reading this post?

Upload files, on webflux server and how handle of it.

I write very simple codes below, so, after you follow that codes. you can handle multiple upload file with handle others.

## Codes

```kotlin
fun uploadImage(serverRequest: ServerRequest): Mono<ServerResponse> {
    val monos = serverRequest.multipartData().flatMap { multipart ->
        // 1. get multipart file
        val files = multipart["file"] ?: listOf()
        // 2. create mono publisher. cause we write this code under flatMap
        return@flatMap Mono.just(files.map { part ->
            val filePart = part.cast<FilePart>()
            // 3. read `DataBuffer` from Flux<DataBuffer> and transform to Mono by reduce using SequenceInputStream
            filePart.content().reduce(object : InputStream() {
                override fun read() = -1
            }) { s: InputStream, d -> SequenceInputStream(s, d.asInputStream(true)) }
                    .flatMap { inputStream ->
                    // 4. after finish read inputStream from flux. read bytes of inputStream. ( ** after fire readBytes function will close your stream. so you can't reuse inputStream )
                        val bytes = inputStream.readBytes() 

                        // 5. now you can use bytes anything you want it. in this example i upload my file on s3 bucket with wrapping Mono.

                        return@flatMap Mono.just(s3Uploader.upload(filePart.filename(), filePart.headers().contentType.toString(), ByteArrayInputStream(bytes), bytes.size.toLong()))
                    }
        })
    }
    return monos.flatMap { responses ->
        // 6. using `Mono zip` for responsing after all files are uploaded.
        Mono.zip(responses, this::resultWithUpload).flatMap {
            // 7. after all of files were uploaded on s3. i response to client.
            ServerResponse.ok().body(BodyInserters.fromValue(it))
        }
    }
}

fun resultWithUpload(results: Array<Any>): List<s3UploadResponse> {
    return results.map { return@map it as s3UploadResponse }.toList()
}
```

## Conclusion

Very simple upload example. now you can handle file with webflux stack.

> _Stay Hunger, Stay Foolish_
