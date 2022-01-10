package com.microservice.core.controller;

import com.microservice.core.model.EmployeeProfile;
import com.microservice.core.service.EmployeeProfileService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/profiles")
public class EmployeeProfileController {
    @Autowired
    private EmployeeProfileService employeeProfileService;

    @GetMapping
    public List<EmployeeProfile> getAllEmployees() {
        return employeeProfileService.getAll();
    }

    @PostMapping
    public void saveEmployee(@RequestBody EmployeeProfile profile){
        employeeProfileService.add(profile);
    }
}
