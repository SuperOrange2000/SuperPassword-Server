package com.superpassword.api.converters;

import com.superpassword.api.dao.InfoGroup;
import com.superpassword.api.dto.InfoGroupDTO;

public class InfoGroupConverter {
    public static InfoGroupDTO convert(InfoGroup infoGroup) {
        InfoGroupDTO infoGroupDTO = new InfoGroupDTO();
        infoGroupDTO.setGuid(infoGroup.getGuid());
        infoGroupDTO.setPassword(infoGroup.getPassword());
        infoGroupDTO.setSite(infoGroup.getSite());
        infoGroupDTO.setUsername(infoGroup.getUsername());
        infoGroupDTO.setExtraInfo(infoGroup.getExtraInfo());
        infoGroupDTO.setUpdateTime(infoGroup.getUpdateTime());
        infoGroupDTO.setCreateTime(infoGroup.getCreateTime());
        return infoGroupDTO;
    }

    public static InfoGroup convert(InfoGroupDTO infoGroupDTO) {
        InfoGroup infoGroup = new InfoGroup();
        infoGroup.setGuid(infoGroupDTO.getGuid());
        infoGroup.setPassword(infoGroupDTO.getPassword());
        infoGroup.setSite(infoGroupDTO.getSite());
        infoGroup.setUsername(infoGroupDTO.getUsername());
        infoGroup.setCreateTime(infoGroupDTO.getCreateTime());
        infoGroup.setUpdateTime(infoGroupDTO.getUpdateTime());
        return infoGroup;
    }
}
