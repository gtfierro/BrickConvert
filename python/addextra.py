from rdflib import Graph, Namespace, URIRef, Literal
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
BRICK = Namespace('https://brickschema.org/schema/1.0.1/Brick#')
BRICKFRAME = Namespace('https://brickschema.org/schema/1.0.1/BrickFrame#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')


g = Graph()
g.bind('rdf', RDF)
g.bind('rdfs', RDFS)
g.bind('brick', BRICK)
g.bind('bf', BRICKFRAME)

g.add((BRICK.Green_Button_Meter, RDF.type, OWL.Class))
g.add((BRICK.Green_Button_Meter, RDFS.subClassOf, BRICK.Building_Electric_Meter))

g.add((BRICK.Building_Electric_Meter, RDF.type, OWL.Class))
g.add((BRICK.Building_Electric_Meter, RDFS.subClassOf, BRICK.Electric_Meter))

g.add((BRICK.RTU, RDFS.subClassOf, BRICK.AHU))
g.add((BRICK.RTU, RDF.type, OWL.Class))

g.add((BRICK.Illumination_Sensor, RDFS.subClassOf, BRICK.Sensor))
g.add((BRICK.Illumination_Sensor, RDF.type, OWL.Class))

g.serialize('extra_classes.ttl',format='turtle')
