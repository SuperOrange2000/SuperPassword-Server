package com.superpassword.api.controller;

import com.superpassword.api.vo.Response;
import com.superpassword.api.dto.InfoGroupDTO;
import com.superpassword.api.service.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class InfoGroupController {

    @Autowired
    private DataService infoGroupService;

    @GetMapping("/infogroup/{id}")
    public Response<InfoGroupDTO> getInfoGroupById(@PathVariable long id) {
        return Response.newSuccess(infoGroupService.getById(id));
    }

    @PostMapping("/infogroup")
    public Response<Long> addNewInfoGroup(@RequestBody InfoGroupDTO infoGroupDTO) {
        return Response.newSuccess(infoGroupService.addNewInfoGroup(infoGroupDTO));
    }
}
