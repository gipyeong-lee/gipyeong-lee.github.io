---
layout: post
title: "Webflux - Multipart File Upload"
style: border
color: danger
description: An example of how to handle multipart file uploads in Spring Webflux.
lang: en
ref: 2020-12-29-Webflux-Multipart
---


## What Will You Learn from This Post?

This post explains how to upload files to a Webflux server and how to handle them effectively.

I have provided some simple code snippets below. By following them, you will be able to handle multiple file uploads along with other request data.

## Code Examples

```kotlin
fun uploadImage(serverRequest: ServerRequest): Mono<ServerResponse> {
    val monos = serverRequest.multipartData().flatMap { multipart ->
        // 1. Retrieve the multipart files
        val files = multipart["file"] ?: listOf()
        
        // 2. Create a Mono publisher (since we are inside a flatMap)
        return@flatMap Mono.just(files.map { part ->
            val filePart = part.cast<FilePart>()
            
            // 3. Read DataBuffers from Flux<DataBuffer> and transform them into a Mono using SequenceInputStream for reduction
            filePart.content().reduce(object : InputStream() {
                override fun read() = -1
            }) { s: InputStream, d -> SequenceInputStream(s, d.asInputStream(true)) }
                    .flatMap { inputStream ->
                        // 4. After reading the InputStream from the Flux, extract the bytes. 
                        // (** Note: readBytes() will close the stream, so it cannot be reused.)
                        val bytes = inputStream.readBytes() 

                        // 5. Now you can use the bytes as needed. In this example, I upload the file to an S3 bucket within a Mono.
                        return@flatMap Mono.just(s3Uploader.upload(filePart.filename(), filePart.headers().contentType.toString(), ByteArrayInputStream(bytes), bytes.size.toLong()))
                    }
        })
    }
    
    return monos.flatMap { responses ->
        // 6. Use Mono.zip to wait for all files to be uploaded before responding.
        Mono.zip(responses, this::resultWithUpload).flatMap {
            // 7. Once all files have been uploaded to S3, return the response to the client.
            ServerResponse.ok().body(BodyInserters.fromValue(it))
        }
    }
}

fun resultWithUpload(results: Array<Any>): List<s3UploadResponse> {
    return results.map { it as s3UploadResponse }.toList()
}
```

## Conclusion

This is a simple example of how to handle file uploads. With this approach, you can now manage multipart files within the Webflux stack.

> _Stay Hungry, Stay Foolish_
