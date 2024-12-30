#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.basesections import (
    CompositeSystem,
    Instrument,
    Measurement,
)
from nomad.metainfo import (
    Datetime,
    Package,
    Quantity,
    Section,
    SubSection,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Data_Entries')


class MetaData(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln=None,
    )
    Spot_Diameter_estimated = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'nm', 'component': 'NumberEditQuantity'},
        unit='nm',
    )
    Stigmator_X = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Stigmator_Y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Beam_Shift_X = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Beam_Shift_Y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Source_Tilt_X = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Source_Tilt_Y = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Emission_Current = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'A', 'component': 'NumberEditQuantity'},
        unit='A',
    )
    Specimen_Current = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'A', 'component': 'NumberEditQuantity'},
        unit='A',
    )
    Scan_Rotation = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'rad', 'component': 'NumberEditQuantity'},
        unit='rad',
    )
    Compound_Lens = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    Compound_Lens_Threshold_Energy = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'eV', 'component': 'NumberEditQuantity'},
        unit='eV',
    )
    Stage_X = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'm', 'component': 'NumberEditQuantity'},
        unit='m',
    )
    Stage_Y = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'm', 'component': 'NumberEditQuantity'},
        unit='m',
    )
    Stage_Z = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'm', 'component': 'NumberEditQuantity'},
        unit='m',
    )
    Stage_Rotation = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'rad', 'component': 'NumberEditQuantity'},
        unit='rad',
    )
    Stage_Tilt_alpha = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'rad', 'component': 'NumberEditQuantity'},
        unit='rad',
    )
    Stage_Tilt_beta = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'rad', 'component': 'NumberEditQuantity'},
        unit='rad',
    )
    Stage_Bias = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'V', 'component': 'NumberEditQuantity'},
        unit='V',
    )
    Chamber_Pressure = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'Pa', 'component': 'NumberEditQuantity'},
        unit='Pa',
    )
    Contrast = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Brightness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Signal_Type = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    Contrast_DB = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'dB', 'component': 'NumberEditQuantity'},
        unit='dB',
    )
    Brightness_DB = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'dB', 'component': 'NumberEditQuantity'},
        unit='dB',
    )
    Average = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Integrate = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Resolution_X = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Resolution_Y = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Horizontal_Fieldsize = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'm', 'component': 'NumberEditQuantity'},
        unit='m',
    )
    Vertical_Fieldsize = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'm', 'component': 'NumberEditQuantity'},
        unit='m',
    )
    Frame_Time = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 's', 'component': 'NumberEditQuantity'},
        unit='s',
    )
    Digital_Contrast = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Digital_Brightness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    Digital_Gamma = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )


class SEM_Image(Measurement, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
                'lab_id',
                'location',
                'steps',
                'samples',
                'instruments',
                'results',
            ]
        },
    )
    Sample = Quantity(
        type=CompositeSystem,
        a_eln={'overview': True},
        shape=['*'],
    )
    Microscope = Quantity(
        type=Instrument,
        a_eln={'overview': True},
    )
    Detector = Quantity(
        type=Instrument,
        a_eln={'overview': True},
    )
    Time_of_Creation = Quantity(
        type=Datetime,
        a_eln={'overview': True},
    )
    Path_to_Image = Quantity(
        type=str,
        a_eln={'overview': True},
    )
    Pixel_Width = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'nm', 'overview': True},
        unit='m',
    )
    Pixel_Height = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'nm', 'overview': True},
        unit='m',
    )
    Acceleration_Voltage = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'kV', 'overview': True},
        unit='V',
    )
    Beam_Current = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'nA', 'overview': True},
        unit='A',
    )
    Working_Distance = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'mm', 'overview': True},
        unit='m',
    )
    Dwell_Time = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'microsecond', 'overview': True},
        unit='s',
    )
    SEM_Mode = Quantity(
        type=str,
        a_eln={'overview': True},
    )
    Stage_Tilt_alpha = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'deg', 'overview': True},
        unit='rad',
    )
    Tilt_Correction = Quantity(
        type=bool,
        a_eln={'overview': True},
    )
    Detector_Mode = Quantity(
        type=str,
        a_eln={'overview': True},
    )
    Meta_Data = SubSection(
        section_def=MetaData,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `SEM_Image` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class SEM_Image_ETD(SEM_Image, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
                'lab_id',
                'location',
                'steps',
                'samples',
                'instruments',
                'results',
            ]
        },
    )
    Grid_Voltage = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'V', 'component': 'NumberEditQuantity'},
        unit='V',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `SEM_Image_ETD` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class SEM_Image_TLD(SEM_Image, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
                'lab_id',
                'location',
                'steps',
                'samples',
                'instruments',
                'results',
            ]
        },
    )
    Suction_Tube_Voltage = Quantity(
        type=np.float64,
        a_eln={'defaultDisplayUnit': 'V', 'component': 'NumberEditQuantity'},
        unit='V',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `SEM_Image_TLD` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


m_package.__init_metainfo__()
