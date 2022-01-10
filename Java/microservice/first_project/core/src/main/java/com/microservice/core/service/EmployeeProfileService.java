package com.microservice.core.service;

import com.microservice.core.model.EmployeeProfile;
import org.springframework.stereotype.Service;

import java.util.List;

public interface EmployeeProfileService {
    List<EmployeeProfile> getAll();

    void add(EmployeeProfile profile);
}
