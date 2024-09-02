package com.superpassword.api.controller;

import com.superpassword.api.exception.DataNotFoundException;
import com.superpassword.api.vo.ErrorCode;
import com.superpassword.api.vo.Response;
import com.superpassword.api.dto.InfoGroupDTO;
import com.superpassword.api.service.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import io.jsonwebtoken.security.SignatureException;

@RestController
@RequestMapping("/info-group")
public class InfoGroupController {

    @Autowired
    private DataService infoGroupService;

    @GetMapping("/{guid}")
    public Response<InfoGroupDTO> getInfoGroupByGuid(@RequestHeader("Authorization") String token, @PathVariable String guid) {
        try {
            return Response.newSuccess(infoGroupService.getByGuid(token, guid));
        } catch (DataNotFoundException e) {
            return Response.newFail(ErrorCode.DATA_NOT_FOUND);
        } catch (SignatureException e) {
            return Response.newFail(ErrorCode.NO_PERMISSION);
        }
    }

    @PostMapping("")
    public Response<Long> addNewInfoGroup(@RequestHeader("Authorization") String token, @RequestBody InfoGroupDTO infoGroupDTO) {
        try {
            return Response.newSuccess(infoGroupService.addNewInfoGroup(token, infoGroupDTO));
        } catch (SignatureException e) {
            return Response.newFail(ErrorCode.NO_PERMISSION);
        }
    }

    @PutMapping("/{guid}")
    public Response<Long> updateInfoGroup(@RequestHeader("Authorization") String token,
                                          @PathVariable String guid,
                                          @RequestParam(required = false) byte[] site,
                                          @RequestParam(required = false) byte[] username,
                                          @RequestParam(required = false) byte[] password) {
        try {
            return Response.newSuccess(infoGroupService.updateInfoGroup(token, guid, site, username, password));
        } catch (DataNotFoundException e) {
            return Response.newFail(ErrorCode.DATA_NOT_FOUND);
        } catch (SignatureException e) {
            return Response.newFail(ErrorCode.NO_PERMISSION);
        }
    }

    @DeleteMapping("/{guid}")
    public Response<Long> deleteInfoGroup(@RequestHeader("Authorization") String token, @PathVariable String guid) {
        try {
            return Response.newSuccess(infoGroupService.deleteInfoGroup(token, guid));
        } catch (DataNotFoundException e) {
            return Response.newFail(ErrorCode.DATA_NOT_FOUND);
        } catch (SignatureException e) {
            return Response.newFail(ErrorCode.NO_PERMISSION);
        }
    }
}
