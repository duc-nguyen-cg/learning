package com.microservice.core.service;

import com.microservice.core.model.EmployeeProfile;
import com.microservice.core.repository.EmployeeProfileRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EmployeeProfileServiceImpl implements EmployeeProfileService{
    @Autowired
    private EmployeeProfileRepository employeeProfileRepository;


    @Override
    public List<EmployeeProfile> getAll() {
        return employeeProfileRepository.findAll();
    }

    @Override
    public void add(EmployeeProfile profile) {
        employeeProfileRepository.save(profile);
    }
}
