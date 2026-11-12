- create an odoo custom addons folder
- add it to the path
- create a module within it
- create the 2 intital folders (views,models)
- add **init**.py in models
- add a py file for your entity and logic
- import all of its content into the init file
- create a view file
- create the manifast
- activate module
- update the apps list
- inspect the database for the new created model
- inspect the automatic fields (created at updated at and so)
- actions (clicking buttons e.g new and so) types are menu, button, contextual object
- menus and sub menus

here if there is not form we cant update the records we can only view them
<field name="view_mode">list,form</field>

- groups layout in creation form
- search view with suspended filter
- students menue with domain filter only suspended show
- create a relation from a student to a student name it friends make it many to many.
- add a computed field to calculate how many friends the student has on the fly
