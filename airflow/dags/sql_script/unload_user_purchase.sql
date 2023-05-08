COPY (
       select invoice_number,
              vendor_id,
              detail,
              tax,
              invoice_date,
              total,
              customer_id,
              country
       from online.user_purchase -- we should have a date filter here to pull only required data
) TO '{{ params.user_purchase }}' WITH (FORMAT CSV, HEADER);