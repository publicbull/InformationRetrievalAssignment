from scrapy.contrib.exporter import XmlItemExporter

class YelpreviewItemXmlExporter(XmlItemExporter):
	def serialize_field(self, field, name, value):
		if type(value) == float or type(value) == int:
			value = str(value)
		return super(YelpreviewItemXmlExporter, self).serialize_field(field, name, value)