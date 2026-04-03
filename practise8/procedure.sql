CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_count INT := 0;
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        -- simple phone validation
        IF phones[i] ~ '^[0-9]{10,15}$' THEN
            INSERT INTO phonebook(name, phone)
            VALUES (names[i], phones[i]);
        ELSE
            invalid_count := invalid_count + 1;
            RAISE NOTICE 'Invalid phone: %', phones[i];
        END IF;
    END LOOP;

    RAISE NOTICE 'Total invalid numbers: %', invalid_count;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value
       OR phone = p_value;
END;
$$;