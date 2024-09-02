package com.superpassword.api.service;

import com.superpassword.api.dto.InfoGroupDTO;

public interface DataService {
    InfoGroupDTO getByGuid(String token, String guid);

    long addNewInfoGroup(String token, InfoGroupDTO infoGroupDTO);

    long updateInfoGroup(String token, String guid, byte[] site, byte[] username, byte[] password);

    long deleteInfoGroup(String token, String guid);
}
