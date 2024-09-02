package com.superpassword.api.dao;

import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "api_infogroup")
public class InfoGroup {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(name = "guid")
    private String guid;
    @Column(name = "site")
    private byte[] site;
    @Column(name = "username")
    private byte[] username;
    @Column(name = "password")
    private byte[] password;

    @Column(name = "create_time")
    private LocalDateTime createTime;
    @Column(name = "update_time")
    private LocalDateTime updateTime;

    @Column(name = "extra_info")
    private byte[] extraInfo = null;

    @Column(name = "owner_id")
    private long owner_id;

    public long getId() {
        return id;
    }

    public byte[] getSite() {
        return site;
    }

    public byte[] getUsername() {
        return username;
    }

    public byte[] getPassword() {
        return password;
    }

    public void setSite(byte[] site) {
        this.site = site;
    }

    public void setUsername(byte[] username) {
        this.username = username;
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

    public long getOwner_id() {
        return owner_id;
    }

    public void setOwnerId(long owner_id) {
        this.owner_id = owner_id;
    }
}
