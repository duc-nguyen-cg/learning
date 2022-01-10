package com.log;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Main {
    private static Logger log = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        for (int i = 0; i < 1000; i ++){
            log.info("info" + i);
            log.warn("warn" + i);
            log.error("error" + i);
        }
    }
}
