INSERT INTO hotels (name,location,services, rooms_quantity, image_id) VALUES 
('Cosmos Collection', 'Anapa', '["Wifi", "Parking", "Pool", "Bar"]', 2, 1),
('New Hotel', 'Moscow', '["Wifi", "Parking", "Pool", "Bar"]', 3, 2),
('Old Hotel', 'Moscow', '["Wifi", "Parking", "Pool", "Bar"]', 4, 3)
;

INSERT INTO rooms (hotel_id, name, price, quantity, services, description, image_id) VALUES
(1, 'Lux', 5000, 2, '["Wifi", "Parking", "Pool", "Bar"]', 'Lux room with a view of the sea', 4),
(1, 'Standart', 3000, 3, '["Wifi", "Parking", "Pool", "Bar"]', 'Standart room with a view of the sea', 5),
(2, 'Lux', 5000, 2, '["Wifi", "Parking", "Pool", "Bar"]', 'Lux room with a view of the city', 6),
(2, 'Standart', 3000, 3, '["Wifi", "Parking", "Pool", "Bar"]', 'Standart room with a view of the city', 7),
(3, 'Lux', 5000, 2, '["Wifi", "Parking", "Pool", "Bar"]', 'Lux room with a view of the city', 8),
(3, 'Standart', 3000, 3, '["Wifi", "Parking", "Pool", "Bar"]', 'Standart room with a view of the city', 9)
;


INSERT INTO users (email, hashed_password) VALUES
('fedor@moloko.ru', 'tut_budet_hashed_password_1'),
('sharik@moloko.ru', 'tut_budet_hashed_password_2');


INSERT INTO bookings (room_id, user_id, date_from, date_to, price) VALUES
(1, 1, '2023-06-15', '2673-06-30', 24500),
(7, 2, '2023-06-25', '2023-07-10', 4300);
