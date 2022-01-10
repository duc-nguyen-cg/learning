package com.microservice.orderservice.repository;

import com.microservice.orderservice.model.OrderProduct;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IOrderProductRepository extends JpaRepository<OrderProduct, Long> {
}
