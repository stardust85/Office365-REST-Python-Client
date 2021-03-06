from office365.runtime.client_object import ClientObject
from office365.runtime.resource_path import ResourcePath
from office365.sharepoint.field_collection import FieldCollection


class ContentType(ClientObject):
    """Specifies a content type."""

    @property
    def fields(self):
        """Gets a value that specifies the collection of fields for the content type."""
        if self.is_property_available('Fields'):
            return self.properties['Fields']
        else:
            return FieldCollection(self.context, ResourcePath("Fields", self.resource_path))

    @property
    def parent(self):
        """Gets the parent content type of the content type."""
        if self.is_property_available('Parent'):
            return self.properties['Parent']
        else:
            return ContentType(self.context, ResourcePath("Parent", self.resource_path))
