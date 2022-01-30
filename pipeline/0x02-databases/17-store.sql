-- Create a trigger to detect orders change an apply this login on item
CREATE TRIGGER up
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
