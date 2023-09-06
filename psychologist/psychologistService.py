import psychologist.psychologistDao as psychologistDao

def getPsychologistList():
    return psychologistDao.getPsychologistInOrder()


def getPsychologistById(psyId):
    return psychologistDao.getPsychologistById(psyId)