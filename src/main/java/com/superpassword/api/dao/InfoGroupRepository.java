package com.superpassword.api.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface InfoGroupRepository extends JpaRepository<InfoGroup, Long> {
}
