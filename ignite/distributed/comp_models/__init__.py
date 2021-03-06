from ignite.distributed.comp_models.base import _SerialModel
from ignite.distributed.comp_models.native import has_native_dist_support
from ignite.distributed.comp_models.xla import has_xla_support


def setup_available_computation_models():
    models = [
        _SerialModel,
    ]
    if has_native_dist_support:
        from ignite.distributed.comp_models.native import _NativeDistModel

        models.append(_NativeDistModel)
    if has_xla_support:
        from ignite.distributed.comp_models.xla import _XlaDistModel

        models.append(_XlaDistModel)

    return tuple(models)


registered_computation_models = setup_available_computation_models()
