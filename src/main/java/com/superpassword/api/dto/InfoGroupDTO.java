package com.superpassword.api.dto;

import java.time.LocalDateTime;

public class InfoGroupDTO {

    private String guid;
    private byte[] site;
    private byte[] username;
    private byte[] password;
    private byte[] extraInfo;

    private LocalDateTime createTime;
    private LocalDateTime updateTime;

    public byte[] getSite() {
        return site;
    }

    public void setSite(byte[] site) {
        this.site = site;
    }

    public byte[] getUsername() {
        return username;
    }

    public void setUsername(byte[] username) {
        this.username = username;
    }

    public byte[] getPassword() {
        return password;
    }

    public void setPassword(byte[] password) {
        this.password = password;
    }

    public LocalDateTime getCreateTime() {
        return createTime;
    }

    public void setCreateTime(LocalDateTime createTime) {
        this.createTime = createTime;
    }

    public LocalDateTime getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(LocalDateTime updateTime) {
        this.updateTime = updateTime;
    }

    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }

    public byte[] getExtraInfo() {
        return extraInfo;
    }

    public void setExtraInfo(byte[] extraInfo) {
        this.extraInfo = extraInfo;
    }
}
