package com.superpassword.api.dao;

import jakarta.persistence.*;

import java.time.LocalDateTime;
import java.util.Date;

@Entity
@Table(name = "api_infogroup")
public class InfoGroup {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

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
}
