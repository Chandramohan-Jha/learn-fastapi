# Create a alembic template
`alembic init -t async migrations`

run a migration
`alembic revision --autogenerate -m "message"`

apply migration
`alembic upgrade head`
