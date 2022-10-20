insert into shipments_company (id, name, country, description, created_at, updated_at)
values ('123e4567-e89b-12d3-a456-426614174000', 'Epam', 'BY', 'Epam is software development company.', '2022-10-20 11:47:14.775000 +00:00', '2022-10-20 11:47:14.775000 +00:00'),
       ('123e4567-e89b-12d3-a456-426614174001', 'LeverX', 'BY', 'LeverX is software development company.', '2022-10-20 11:47:14.775000 +00:00', '2022-10-20 11:47:14.775000 +00:00'),
       ('123e4567-e89b-12d3-a456-426614174002', 'Solbeg', 'BY', 'Solbeg is software development company.', '2022-10-20 11:47:14.775000 +00:00', '2022-10-20 11:47:14.775000 +00:00');

insert into shipments_shipment (id, title, delivery_country, description, quantity, created_at, updated_at, availability, delivery_status, company_id)
values ('123e4567-e89b-12d3-a456-426614174003', 'Keyboards', 'PL', 'Keyboards for the dev team in new office', 25, '2022-10-20 11:47:14.775000 +00:00', '2022-10-20 11:47:14.775000 +00:00', 'AVAILABLE', 'CREATED', '123e4567-e89b-12d3-a456-426614174000'),
       ('123e4567-e89b-12d3-a456-426614174004', 'Keyboards', 'PL', 'Keyboards for the dev team in new office', 50, '2022-10-20 11:47:14.775000 +00:00', '2022-10-20 11:47:14.775000 +00:00', 'AVAILABLE', 'CREATED', '123e4567-e89b-12d3-a456-426614174001'),
       ('123e4567-e89b-12d3-a456-426614174005', 'Keyboards', 'PL', 'Keyboards for the dev team in new office', 40, '2022-10-20 11:47:14.775000 +00:00', '2022-10-20 11:47:14.775000 +00:00', 'AVAILABLE', 'CREATED', '123e4567-e89b-12d3-a456-426614174002');