#! python3
# Wrappers to unify interactions with the different kinds of docs to be found in PTP

def openPTPDoc(filename):
    if filename.endswith(".doc"):
        pass
    elif filename.endswith(".docx"):
        pass
    elif filename.endswith(".pdf"):
        pass
    else:
        raise TypeError("File is not a .doc, .docx, nor .pdf")
    
def identifyPTPDoc(filename):
    '''Given a string filename, return a string with the type of PTP document (Discharge, Pscyhology, Psychiatry),
    or Unidentified if not able to determine.'''
    docIdentity = "Unidentified"
    if "-ds." in filename:
        docIdentity = "Discharge"
    elif "-final." in filename:
        docIdentity = "Psychology"
    elif "-md." in filename:
        docIdentity = "Psychiatry"
    elif "-joint." in filename:
        docIdentity = "Joint"
    return docIdentity