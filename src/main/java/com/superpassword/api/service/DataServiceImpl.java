package com.superpassword.api.service;

import com.superpassword.api.converter.InfoGroupConverter;
import com.superpassword.api.dao.InfoGroup;
import com.superpassword.api.dao.InfoGroupRepository;
import com.superpassword.api.dao.User;
import com.superpassword.api.dto.InfoGroupDTO;
import com.superpassword.api.exception.DataNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
public class DataServiceImpl implements DataService {
    @Autowired
    private InfoGroupRepository infoGroupRepository;

    @Autowired
    private LoginService loginService;

    @Override
    public InfoGroupDTO getByGuid(String token, String guid) {
        User owner = loginService.getUserInfoByToken(token);
        InfoGroup infoGroup = infoGroupRepository.findByGuid(guid).orElseThrow(DataNotFoundException::new);
        if (infoGroup.getOwner_id() != owner.getId())
            throw new DataNotFoundException();
        return InfoGroupConverter.convert(infoGroup);
    }

    @Override
    public long addNewInfoGroup(String token, InfoGroupDTO infoGroupDTO) {
        User owner = loginService.getUserInfoByToken(token);
        infoGroupDTO.setCreateTime(LocalDateTime.now());
        infoGroupDTO.setUpdateTime(LocalDateTime.now());

        InfoGroup infoGroup = InfoGroupConverter.convert(infoGroupDTO);
        infoGroup.setOwnerId(owner.getId());

        infoGroupRepository.save(infoGroup);
        return infoGroup.getId();
    }

    @Override
    @Transactional
    public long updateInfoGroup(String token, String guid, byte[] site, byte[] username, byte[] password) {
        InfoGroup infoGroup = infoGroupRepository.findByGuid(guid).orElseThrow(DataNotFoundException::new);
        boolean modifyFlag = false;
        if (site != null) {
            infoGroup.setSite(site);
            modifyFlag = true;
        }
        if (username != null) {
            infoGroup.setUsername(username);
            modifyFlag = true;
        }
        if (password != null) {
            infoGroup.setPassword(password);
            modifyFlag = true;
        }
        if (modifyFlag) {
            infoGroup.setUpdateTime(LocalDateTime.now());
            infoGroupRepository.save(infoGroup);
        }
        return infoGroup.getId();
    }

    @Override
    public long deleteInfoGroup(String token, String guid) {
        InfoGroup infoGroup = infoGroupRepository.findByGuid(guid).orElseThrow(DataNotFoundException::new);
        infoGroupRepository.delete(infoGroup);
        return infoGroup.getId();
    }
}
