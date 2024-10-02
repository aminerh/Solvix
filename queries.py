
# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *



def commande_relance(order,old_state,new_state,commentaire) :
    # Start a connection and transaction
  try: 
    with SolviXengine.connect() as connection:
        # Start a transaction
        trans = connection.begin()
        try:
            insert_query = text("""
                INSERT INTO public.order_actions_log (order_id, action, user_id, old_value, new_value, state, remarks) 
                VALUES (:order_id, 'Waved', :user, 'init state', :new_state, 1, :remarks)
            """)

            # Correct the parameter dictionary (no colons in the keys)
            connection.execute(insert_query, {
                'order_id': order,
                'user': user,
                'new_state': new_state,
                'remarks': commentaire
            })
            print(f"Wave done for order_id: {order}")

            # Commit the transaction
            trans.commit()
        except Exception as e:
            # If any error occurs, rollback the transaction
            trans.rollback()
            print(f"Error during transaction: {e}")

  except SQLAlchemyError as e:
    print(f"Error executing SQL: {e}")
