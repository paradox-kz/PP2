-- ======================
-- ADD PHONE
-- ======================
CREATE OR REPLACE PROCEDURE add_phone(
    p_name TEXT,
    p_phone TEXT,
    p_type TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE 
    cid INT;
BEGIN
    -- найти контакт
    SELECT id INTO cid FROM contacts WHERE name = p_name;

    -- если нет — создать
    IF cid IS NULL THEN
        INSERT INTO contacts(name)
        VALUES (p_name)
        RETURNING id INTO cid;
    END IF;

    -- добавить телефон
    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;


-- ======================
-- MOVE TO GROUP
-- ======================
CREATE OR REPLACE PROCEDURE move_to_group(
    p_name TEXT,
    p_group TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE 
    gid INT;
BEGIN
    -- создать группу если нет
    INSERT INTO groups(name)
    VALUES (p_group)
    ON CONFLICT (name) DO NOTHING;

    -- получить id
    SELECT id INTO gid FROM groups WHERE name = p_group;

    -- обновить контакт
    UPDATE contacts
    SET group_id = gid
    WHERE name = p_name;
END;
$$;


-- ======================
-- SEARCH
-- ======================
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(name TEXT, email TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$;