package com.superpassword.api.service;

import com.superpassword.api.dto.InfoGroupDTO;

import io.jsonwebtoken.security.SignatureException;

public interface DataService {
    InfoGroupDTO getByGuid(String token, String guid) throws SignatureException;

    long addNewInfoGroup(String token, InfoGroupDTO infoGroupDTO) throws SignatureException;

    long updateInfoGroup(String token, String guid, byte[] site, byte[] username, byte[] password);

    long deleteInfoGroup(String token, String guid);
}
