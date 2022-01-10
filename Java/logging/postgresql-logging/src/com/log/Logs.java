package com.log;

public class Logs {
    private Long logsId;
    private String levelLog;
    private String content;

    public Long getLogsId() {
        return logsId;
    }

    public void setLogsId(Long logsId) {
        this.logsId = logsId;
    }

    public String getLevelLog() {
        return levelLog;
    }

    public void setLevelLog(String levelLog) {
        this.levelLog = levelLog;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
