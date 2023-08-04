from abc import ABC, abstractmethod
from typing import Any, List, Tuple

from ipyvizzu.data.infer_type import InferType
from ipyvizzu.data.typing_alias import (
    DimensionValue,
    MeasureValue,
    Series,
    SeriesValues,
)


class ToSeriesListConverter(ABC):
    @abstractmethod
    def get_series_list(self) -> List[Series]:
        """
        Convert data to a list of dictionaries representing series.

        Returns:
            A list of dictionaries representing series,
            where each dictionary has `name`, `values` and `type` keys.
        """

    @abstractmethod
    def _convert_to_series_values_and_type(
        self, object: Any
    ) -> Tuple[SeriesValues, InferType]:
        """
        Convert object to SeriesValues and InferType.
        """

    @abstractmethod
    def _convert_to_measure_values(self, object: Any) -> List[MeasureValue]:
        """
        Convert object to a list of MeasureValue.
        """

    @abstractmethod
    def _convert_to_dimension_values(self, object: Any) -> List[DimensionValue]:
        """
        Convert object to a list of DimensionValue.
        """

    def _convert_to_series(
        self, name: str, values: SeriesValues, infer_type: InferType
    ) -> Series:
        return {
            "name": str(name),
            "values": values,
            "type": infer_type.value,
        }
