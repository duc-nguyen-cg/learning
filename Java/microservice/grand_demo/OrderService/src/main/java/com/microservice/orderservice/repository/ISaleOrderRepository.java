package com.microservice.orderservice.repository;

import com.microservice.orderservice.model.SaleOrder;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ISaleOrderRepository extends JpaRepository<SaleOrder, Long> {
}
