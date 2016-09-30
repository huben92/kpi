# coding: utf-8
from rest_framework import serializers
from rest_framework.reverse import reverse

import report_data


class ReportsListSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        request = self.context['request']
        return {
            'url': reverse('reports-detail', args=(obj.uid,), request=request),
        }


class ReportsDetailSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        request = self.context['request']
        if 'names' in request.query_params:
            vnames = filter(lambda x: len(x) > 1,
                            request.query_params.get('names', '').split(','))
        else:
            vnames = None
        _list = report_data.data_by_identifiers(obj, vnames)

        return {
            'url': reverse('reports-detail', args=(obj.uid,), request=request),
            'count': len(_list),
            'list': _list,
        }