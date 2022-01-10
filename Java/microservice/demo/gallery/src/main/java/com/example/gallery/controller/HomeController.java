package com.example.gallery.controller;

import com.example.gallery.model.Gallery;
import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;
import java.util.List;


@RestController
@RequestMapping("/galleries")
public class HomeController {

    private static final Logger LOGGER = LoggerFactory.getLogger(HomeController.class);

    @Autowired
    private Environment env;

    @Autowired
    private RestTemplate restTemplate;

    @GetMapping
    public String home() {
        return "Hello from Gallery Service running at port:"+ env.getProperty("local.server.port");
    }

    @GetMapping("/{id}")
    @HystrixCommand(fallbackMethod = "fallback")
    public Gallery getGallery(@PathVariable Long id){
        LOGGER.info("Creating gallery object ... ");
        Gallery gallery = new Gallery();
        gallery.setId(id);

        @SuppressWarnings("unchecked")
        List<Object> images = restTemplate.getForObject("http://image-service/images/", List.class);
        gallery.setImages(images);

        LOGGER.info("Returning images ... ");
        return gallery;
    }

    //backup method returns a default value
    public Gallery fallback(Long galleryId, Throwable hystrixCommand){
        return new Gallery(galleryId);
    }

}
