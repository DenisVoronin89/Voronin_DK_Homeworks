from django.db import models

class Ingredient(models.Model):
    cas_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(null=False)
    id = models.AutoField(primary_key=True)
    inci_name = models.CharField(max_length=255, blank=True, null=True)
    more_info = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    organic = models.BooleanField()
    pubmed_count = models.IntegerField(blank=True, null=True)
    pubmed_term = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(null=False)
    usage = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class IngredientAliasName(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_alias_names')
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Hazard(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='hazards')
    benefit = models.BooleanField()
    created_at = models.DateTimeField(null=False)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(null=False)

    def __str__(self):
        return self.name


class WarningAgency(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='warning_agencies')
    created_at = models.DateTimeField(null=False)
    id = models.AutoField(primary_key=True)
    jurisdiction = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(null=False)

    def __str__(self):
        return self.name


class Source(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='sources')
    created_at = models.DateTimeField(null=False)
    id = models.AutoField(primary_key=True)
    link = models.URLField(blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(null=False)

    def __str__(self):
        return self.name

