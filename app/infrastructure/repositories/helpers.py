def doc_to_user(doc):
  doc["id"] = str(doc["_id"])
  doc.pop("_id")
  return doc

def docs_to_users(docs):
  return [doc_to_user(doc) for doc in docs]