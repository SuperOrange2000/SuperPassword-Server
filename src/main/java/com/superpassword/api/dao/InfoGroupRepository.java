package com.superpassword.api.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface InfoGroupRepository extends JpaRepository<InfoGroup, Long> {
    Optional<InfoGroup> findByGuid(String guid);
}
