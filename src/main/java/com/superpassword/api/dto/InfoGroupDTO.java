package com.superpassword.api.dto;

import com.alibaba.fastjson2.JSONReader;
import com.alibaba.fastjson2.JSONWriter;
import com.alibaba.fastjson2.annotation.JSONField;

import java.time.LocalDateTime;

public class InfoGroupDTO {

    private String guid;
    @JSONField(serializeFeatures = JSONWriter.Feature.WriteByteArrayAsBase64, deserializeFeatures = JSONReader.Feature.Base64StringAsByteArray)
    private byte[] site;
    @JSONField(serializeFeatures = JSONWriter.Feature.WriteByteArrayAsBase64, deserializeFeatures = JSONReader.Feature.Base64StringAsByteArray)
    private byte[] username;
    @JSONField(serializeFeatures = JSONWriter.Feature.WriteByteArrayAsBase64, deserializeFeatures = JSONReader.Feature.Base64StringAsByteArray)
    private byte[] password;
    @JSONField(serializeFeatures = JSONWriter.Feature.WriteByteArrayAsBase64, deserializeFeatures = JSONReader.Feature.Base64StringAsByteArray)
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
