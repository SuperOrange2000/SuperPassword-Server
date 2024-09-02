package com.superpassword.api.service;

import com.superpassword.api.dto.InfoGroupDTO;

public interface DataService {
    public InfoGroupDTO getByGuid(String token, String guid);

    public long addNewInfoGroup(String token, InfoGroupDTO infoGroupDTO);

    public long updateInfoGroup(String token, String guid, byte[] site, byte[] username, byte[] password);

    public long deleteInfoGroup(String token, String guid);
}
