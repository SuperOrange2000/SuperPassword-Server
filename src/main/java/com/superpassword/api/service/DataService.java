package com.superpassword.api.service;

import com.superpassword.api.dto.InfoGroupDTO;

public interface DataService {
    public InfoGroupDTO getById(long id);

    public long addNewInfoGroup(InfoGroupDTO infoGroupDTO);

}
