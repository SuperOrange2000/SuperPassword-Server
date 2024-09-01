package com.superpassword.api.service;

import com.superpassword.api.converters.InfoGroupConverter;
import com.superpassword.api.dao.InfoGroup;
import com.superpassword.api.dao.InfoGroupRepository;
import com.superpassword.api.dto.InfoGroupDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class DataServiceImpl implements DataService {
    @Autowired
    private InfoGroupRepository infoGroupRepository;

    @Override
    public InfoGroupDTO getById(long id) {
        InfoGroup infoGroup = infoGroupRepository.findById(id).orElseThrow(RuntimeException::new);
        return InfoGroupConverter.convert(infoGroup);
    }

    @Override
    public long addNewInfoGroup(InfoGroupDTO infoGroupDTO) {
        infoGroupDTO.setCreateTime(LocalDateTime.now());
        infoGroupDTO.setUpdateTime(LocalDateTime.now());
        InfoGroup infoGroup = infoGroupRepository.save(InfoGroupConverter.convert(infoGroupDTO));
        return infoGroup.getId();
    }
}
