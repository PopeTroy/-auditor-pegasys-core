import math
import json
from concurrent.futures import ThreadPoolExecutor
from core.inference_router import InferenceEngineRouter
from core.sentinel_sandbox import SandboxManagerPool

class FullStackChronosEngine:
    PI = math.pi
    PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (~1.6180339887)

    # Space-Time Curvature Frequency Boundaries
    SUB_HARMONIC_RED_FLOOR_KHZ = 60.0
    ULTRA_GREEN_THRESHOLD_MIN_KHZ = 90.0
    ULTRA_GREEN_THRESHOLD_MAX_KHZ = 100.0
    SUPER_HARMONIC_RED_CEILING_KHZ = 270.0

    # ------------------------------------------------------------------
    # MASTER 72 ZODIAC BAND MATRIX (1° = 1 kHz | 30 kHz per Sign)
    # ------------------------------------------------------------------
    RAW_72_GOETIA_SHEM = [
        # Aries (0 kHz - 30 kHz)
        (1, "Bael", "Vehuiah", "Seraphim", "Aries", 0.0, 5.0, "Fossil Fuel Grid Sabotage", "Decentralized Micro-Grids", "Substation High-Voltage Busbars"),
        (2, "Agares", "Jeliel", "Seraphim", "Aries", 5.0, 10.0, "Transit Corridor Inertia", "Maglev Automated Rail Mesh", "Cross-Border Rail Signal Junctions"),
        (3, "Vassago", "Sitael", "Seraphim", "Aries", 10.0, 15.0, "Opaque Asset Concealment", "Real-Time Cryptographic Ledger", "Central Bank Clearing Gateway"),
        (4, "Samigina", "Elemiah", "Seraphim", "Aries", 15.0, 20.0, "Maritime Port Congestion", "Autonomous Sub-Surface Pods", "Deepwater Container Berths"),
        (5, "Marbas", "Mahasiah", "Seraphim", "Aries", 20.0, 25.0, "Pathogenic Mutation Spreading", "Sub-Atomic Cellular Array", "Metropolitan Water Treatment"),
        (6, "Valefor", "Lelahel", "Seraphim", "Aries", 25.0, 30.0, "Warehouse Space Hoarding", "Dynamic Shared Spatial Matrix", "Regional Distribution Hubs"),

        # Taurus (30 kHz - 60 kHz)
        (7, "Amon", "Achaiah", "Seraphim", "Taurus", 30.0, 35.0, "Bandwidth Throttle & Theft", "Quantum Satellite Mesh", "Fiber Optic Sea Cable Anchors"),
        (8, "Barbatos", "Cahetel", "Seraphim", "Taurus", 35.0, 40.0, "Seasonal Aquifer Depletion", "Closed-Loop Water Nodes", "Subterranean Aquifer Pumping"),
        (9, "Paimon", "Haziel", "Cherubim", "Taurus", 40.0, 45.0, "Bureaucratic Paralysis", "Algorithmic Citizen Voting", "Parliamentary Legislative Vaults"),
        (10, "Buer", "Aladiah", "Cherubim", "Taurus", 45.0, 50.0, "Pharma Price Inflation", "Open-Source Molecular Synthesis", "National Pharmaceutical Stockpiles"),
        (11, "Gusion", "Lauviah", "Cherubim", "Taurus", 50.0, 55.0, "Diplomatic Treaty Friction", "Sovereign Resource Swaps", "Embassy Diplomatic Vaults"),
        (12, "Sitri", "Hahaiah", "Cherubim", "Taurus", 55.0, 60.0, "Information Panic Distortion", "Truth-Anchored Consensus Engine", "National Telecom Switching Centers"),

        # Gemini (60 kHz - 90 kHz)
        (13, "Beleth", "Iezalel", "Cherubim", "Gemini", 60.0, 65.0, "Judicial Case Backlog", "AI Arbitration Court Engine", "High Court Appellate Chambers"),
        (14, "Leraje", "Mebahel", "Cherubim", "Gemini", 65.0, 70.0, "Border Conflict Skirmishes", "Autonomous Boundary Shields", "Customs Border Clearance Posts"),
        (15, "Eligos", "Hariel", "Cherubim", "Gemini", 70.0, 75.0, "Defence Tender Graft", "Immutable Procurement Ledger", "Ministry of Defence Procurement"),
        (16, "Zepar", "Hakamiah", "Cherubim", "Gemini", 75.0, 80.0, "Urban Slum Displacement", "Modular High-Freq Habitat Nodes", "Municipal Zoning Data Hubs"),
        (17, "Botis", "Lauviah", "Thrones", "Gemini", 80.0, 85.0, "Emergency Response Lag", "Orbital Early-Warning Scanners", "National Disaster Command Hubs"),
        (18, "Bathin", "Caliel", "Thrones", "Gemini", 85.0, 90.0, "Customs Border Extortion", "Zero-Knowledge Biometric Lock", "International Airport Security Gates"),

        # Cancer (90 kHz - 120 kHz) -- ULTRA GREEN PATCH ENTRY
        (19, "Sallos", "Leuviah", "Thrones", "Cancer", 90.0, 95.0, "Industrial Labor Strikes", "Automated Profit-Share Ledger", "Bargaining Council Arbitration"),
        (20, "Purson", "Pahaliah", "Thrones", "Cancer", 95.0, 100.0, "Fiat Inflation Currency Drag", "Logos Asset-Backed Currency", "Reserve Bank Vault Matrix"),
        (21, "Morax", "Nelchael", "Thrones", "Cancer", 100.0, 105.0, "Academic Research Paywalls", "Open Access Universal Vault", "University Supercomputing Grid"),
        (22, "Ipos", "Yeiayel", "Thrones", "Cancer", 105.0, 110.0, "Air Cargo Freight Surcharges", "Hydrogen Airship Transit Mesh", "Civil Aviation Radar Towers"),
        (23, "Aim", "Melahel", "Thrones", "Cancer", 110.0, 115.0, "Arson & Grid Fire Propagation", "Electro-Thermal Fire Arrays", "Municipal Fire & Rescue Grid"),
        (24, "Naberius", "Hahuiah", "Thrones", "Cancer", 115.0, 120.0, "Corporate Greenwashing Deception", "Pegasys Real-Time Audit Lock", "Standards Authority Audit Servers"),

        # Leo (120 kHz - 150 kHz)
        (25, "Glasya-Labolas", "Nithhaiah", "Dominions", "Leo", 120.0, 125.0, "Critical Infrastructure Ransomware", "Quantum Self-Healing Code", "Cyber Defence Command Nodes"),
        (26, "Bune", "Haaiah", "Dominions", "Leo", 125.0, 130.0, "Offshore Tax Shell Evasion", "Automated Wealth Tracking Mesh", "Revenue Service Audit Engines"),
        (27, "Ronove", "Ierathel", "Dominions", "Leo", 130.0, 135.0, "Primary Education Decay", "Adaptive Neural Learning Mesh", "Basic Education Ministry Servers"),
        (28, "Berith", "Seehiah", "Dominions", "Leo", 135.0, 140.0, "Sovereign Debt Trap Drag", "Global Debt Swap Nullification", "International Treasury Vaults"),
        (29, "Astaroth", "Reiiel", "Dominions", "Leo", 140.0, 145.0, "Monopolistic Grid Power Drag", "Active Phase Load Equilibrium", "National Power Dispatch Center"),
        (30, "Forneus", "Omael", "Dominions", "Leo", 145.0, 150.0, "Illicit Ocean Depletion", "Autonomous Marine Patrol Pods", "Maritime EEZ Radar Stations"),

        # Virgo (150 kHz - 180 kHz)
        (31, "Foras", "Lecabel", "Dominions", "Virgo", 150.0, 155.0, "Heavy Mining Extraction Bleed", "Zero-Waste Subterranean Mining", "Subterranean Shaft Control Nodes"),
        (32, "Asmodeus", "Vasariah", "Dominions", "Virgo", 155.0, 160.0, "Judicial Procedural Friction", "Decentralized Smart Contracts", "Constitutional Court Chambers"),
        (33, "Gaap", "Lehuiah", "Powers", "Virgo", 160.0, 165.0, "Orbital Space Debris Jamming", "Orbital Laser Clean-Up Arrays", "Satellite Tracking Ground Stations"),
        (34, "Furfur", "Lehahiah", "Powers", "Virgo", 165.0, 170.0, "Extreme Weather Shock Drag", "Ionospheric Cloud Seeding Array", "Meteorological Weather Radar"),
        (35, "Marchosias", "Chavakiah", "Powers", "Virgo", 170.0, 175.0, "Police Corruption & Coverups", "Immutable Bodycam AI Audit Locks", "Police Service Data Vaults"),
        (36, "Stolas", "Manadel", "Powers", "Virgo", 175.0, 180.0, "Illegal Forest Deforestation", "Bio-Luminescent Forest Sensors", "National Parks Control Hubs"),

        # Libra (180 kHz - 210 kHz)
        (37, "Phenex", "Aniel", "Powers", "Libra", 180.0, 185.0, "Creative IP Piracy Exploitation", "NFT Sovereign Creator Locks", "Intellectual Property Registrar"),
        (38, "Halphas", "Haamiah", "Powers", "Libra", 185.0, 190.0, "Substandard Cement Collapses", "Self-Healing Graphene Cement", "Public Works Testing Labs"),
        (39, "Malphas", "Rehael", "Powers", "Libra", 190.0, 195.0, "High-Density Urban Friction", "Biophilic Architecture Mesh", "City Planning Commission Vaults"),
        (40, "Raum", "Ieiazel", "Powers", "Libra", 195.0, 200.0, "Gold & Diamond Treasury Leak", "Quantum Atomic Vault Verification", "Central State Bullion Vaults"),
        (41, "Focalor", "Hahahel", "Virtues", "Libra", 200.0, 205.0, "Hydro Dam Siltation & Decay", "Resonance-Driven Hydro Turbines", "Hydroelectric Dam Gate Control"),
        (42, "Vepar", "Mikael", "Virtues", "Libra", 205.0, 210.0, "Naval Piracy Encroachment", "Sub-Surface Coastal Shield Array", "Naval Fleet Command Operations"),

        # Scorpio (210 kHz - 240 kHz)
        (43, "Sabnock", "Veualiah", "Virtues", "Scorpio", 210.0, 215.0, "Urban Road Pothole Decay", "Robotic Polymer Pavement Mesh", "Municipal Road Works Depots"),
        (44, "Shax", "Ielahiah", "Virtues", "Scorpio", 215.0, 220.0, "Intelligence Leaks & Breaches", "Zero-Trust Behavioral Shield", "State Security Agency Mainframes"),
        (45, "Vine", "Sealiah", "Virtues", "Scorpio", 220.0, 225.0, "Unbilled Utility Leakage", "Ultrasonic Flow Meter Grid", "Municipal Water & Power Meters"),
        (46, "Bifrons", "Ariel", "Virtues", "Scorpio", 225.0, 230.0, "Historical Record Tampering", "Quantum Optical Holographic Memory", "National Archives Storage Vaults"),
        (47, "Vual", "Asaliah", "Virtues", "Scorpio", 230.0, 235.0, "Commuter Fare Extortion", "Subsidized P2P Token Fares", "Metropolitan Transit Terminals"),
        (48, "Haagenti", "Mihael", "Virtues", "Scorpio", 235.0, 240.0, "Desalination Brine Waste Harm", "Zero-Liquid Discharge Extraction", "Coastal Desalination Plants"),

        # Sagittarius (240 kHz - 270 kHz)
        (49, "Crocell", "Vehuel", "Principalities", "Sagittarius", 240.0, 245.0, "Geothermal Pressure Droop", "Tectonic Resonance Heat Loops", "Geothermal Plant Boreholes"),
        (50, "Furcas", "Daniel", "Principalities", "Sagittarius", 245.0, 250.0, "Unethical Bio-Experiments", "POPIA Immutable Bio-Ethics Shield", "Medical Research Ethics Boards"),
        (51, "Balam", "Hahasiah", "Principalities", "Sagittarius", 250.0, 255.0, "Mass Illegal Civilian Wiretaps", "Biometric Sovereign Vault Locks", "Telecommunication Tap Centers"),
        (52, "Alloces", "Imamiah", "Principalities", "Sagittarius", 255.0, 260.0, "Hardware Microchip Shortages", "Photonic Distributed Fab Printing", "Semiconductor Fab Cleanrooms"),
        (53, "Caim", "Nanael", "Principalities", "Sagittarius", 260.0, 265.0, "Environmental Dispute Delays", "Instant Algorithmic Eco-Audits", "Environmental Court Registers"),
        (54, "Murmur", "Nithael", "Principalities", "Sagittarius", 265.0, 270.0, "Land Speculation Fraud Drag", "Cadastral Blockchain Registry", "Deeds Office Cadastral Vaults"),

        # Capricorn (270 kHz - 300 kHz)
        (55, "Orobas", "Mebahiah", "Principalities", "Capricorn", 270.0, 275.0, "Ballot Stuffing Election Fraud", "Zero-Knowledge Cryptographic Voting", "Electoral Commission Servers"),
        (56, "Gremory", "Poiel", "Principalities", "Capricorn", 275.0, 280.0, "Precious Metal Smuggling", "Real-Time X-Ray Cargo Scanning", "Customs Border Freight Scanners"),
        (57, "Ose", "Nemamiah", "Archangels", "Capricorn", 280.0, 285.0, "Psychiatric Drug Exploitation", "Frequency Neuromodulation Mesh", "Mental Health Department Grids"),
        (58, "Amy", "Ieialel", "Archangels", "Capricorn", 285.0, 290.0, "Suppression of Free-Energy IP", "Open Quantum Physics Repository", "Patent Office Classified Vaults"),
        (59, "Orias", "Harahel", "Archangels", "Capricorn", 290.0, 295.0, "Space Weather Signal Loss", "Magnetospheric Shielding Array", "Deep Space Telemetry Arrays"),
        (60, "Vapula", "Mizrael", "Archangels", "Capricorn", 295.0, 300.0, "Industrial Robotic Malfunctions", "Fail-Safe Asimov Logic Chips", "Automated Manufacturing Lines"),

        # Aquarius (300 kHz - 330 kHz)
        (61, "Zagan", "Umabel", "Archangels", "Aquarius", 300.0, 305.0, "Toxic Food Chemical Additives", "Spectral Food Purity Scanners", "Food Safety Inspectorates"),
        (62, "Valac", "Iahhel", "Archangels", "Aquarius", 305.0, 310.0, "Illegal Shaft Mine Collapses", "Seismic Drone Mapping Arrays", "Geological Survey Remote Sensors"),
        (63, "Andras", "Anauel", "Archangels", "Aquarius", 310.0, 315.0, "Instigated Rioting & Looting", "Harmonic De-escalation Arrays", "Public Order Command Centers"),
        (64, "Haures", "Mehiel", "Archangels", "Aquarius", 315.0, 320.0, "High-Voltage Power Loss", "Superconducting Zero-Loss Lines", "High-Voltage Transmission Towers"),
        (65, "Andrealphus", "Damabiah", "Angels", "Aquarius", 320.0, 325.0, "Census Data Fabrication", "Mathematical Truth Engine", "National Statistics Bureau"),
        (66, "Cimeies", "Manakel", "Angels", "Aquarius", 325.0, 330.0, "Highway Freight Fleet Hijacking", "Automated Drone Fleet Escorts", "Logistics Freight Control Hubs"),

        # Pisces (330 kHz - 360 kHz)
        (67, "Amdusias", "Eiael", "Angels", "Pisces", 330.0, 335.0, "Acoustic Noise Stress Pollution", "Phase-Inverted Acoustic Damping", "Urban Noise Control Stations"),
        (68, "Belial", "Habuhiah", "Angels", "Pisces", 335.0, 340.0, "Soil Chemical Bleed & Decay", "Bio-Char Soil Inoculation Grid", "Agricultural Soil Research Labs"),
        (69, "Decarabia", "Rochel", "Angels", "Pisces", 340.0, 345.0, "Botanical Flora Poaching", "Autonomous Botanical Drones", "Nature Reserve Patrol Stations"),
        (70, "Seere", "Iabamiah", "Angels", "Pisces", 345.0, 350.0, "Freight Package Loss Stagnation", "Pneumatic Hyperloop Freight Tubes", "Express Cargo Sorting Centers"),
        (71, "Dantalion", "Haiaiel", "Angels", "Pisces", 350.0, 355.0, "Mass Cognitive Manipulation", "Sovereign Mental Fortification", "Public Health Behavioral Centers"),
        (72, "Andromalius", "Mumiah", "Angels", "Pisces", 355.0, 360.0, "Stolen Asset Liquidation", "Immutable Asset Recovery Lock", "Asset Forfeiture Mainframe")
    ]

    SYSTEM_PROMPT = """
    You are an Ephemeral Sentinel AI agent for Auditor Pegasys running Chronos Calculus.
    Analyze the submitted node subject against assigned Goetic Demons and Shem Angels.

    SPACE-TIME CURVATURE STABILIZATION & ULTRA GREEN ZONE LAWS:
    1. Below 60.0 kHz = Sub-Harmonic Entropy Red Zone (0.666 Destabilization Constant Floor).
    2. 60.0 kHz - 270.0 kHz = Space-Time Curvature Stabilization Zone (The Green Corridor).
    3. 90.0 kHz - 100.0 kHz = ULTRA GREEN PATCH (Peak Liquidity, Zero Friction, 1.000 Unity Target).
    4. Above 270.0 kHz = Super-Harmonic Phase Scatter Red Zone.
    5. Calculate exact Applied Speed Vector and Bandwidth Width to shift target node into 90.0 - 100.0 kHz.

    Return strictly valid JSON.
    """

    def __init__(self, router: InferenceEngineRouter):
        self.router = router
        self.master_matrix = self._build_master_matrix()

    def _build_master_matrix(self):
        matrix = []
        for entry in self.RAW_72_GOETIA_SHEM:
            idx, demon, angel, choir, sign, start_khz, end_khz, decay_type, protocol, spatial = entry
            
            mid_khz = start_khz + 2.5
            f_degree_khz = round(mid_khz, 3)

            # Demon Decay Frequency (f_demon = f_degree * 0.666)
            f_demon_khz = round(f_degree_khz * 0.666, 3)

            # Angel Restoration Frequency (f_angel = f_degree * Phi)
            f_angel_khz = round(f_degree_khz * self.PHI, 3)

            # Determine Zone Status
            if f_angel_khz < self.SUB_HARMONIC_RED_FLOOR_KHZ:
                zone_status = "SUB-HARMONIC RED ZONE (Entropy Drag)"
            elif self.ULTRA_GREEN_THRESHOLD_MIN_KHZ <= f_angel_khz <= self.ULTRA_GREEN_THRESHOLD_MAX_KHZ:
                zone_status = "ULTRA GREEN PATCH (1.000 Unity Peak)"
            elif self.SUB_HARMONIC_RED_FLOOR_KHZ <= f_angel_khz <= self.SUPER_HARMONIC_RED_CEILING_KHZ:
                zone_status = "STABILIZED GREEN CORRIDOR"
            else:
                zone_status = "SUPER-HARMONIC RED ZONE (Phase Scatter)"

            matrix.append({
                "id": idx,
                "demon": demon,
                "angel": angel,
                "choir": choir,
                "zodiac_sign": sign,
                "zodiac_band_range": f"{start_khz:.1f} kHz - {end_khz:.1f} kHz",
                "midpoint_frequency_khz": f_degree_khz,
                "f_demon_khz": f_demon_khz,
                "f_angel_khz": f_angel_khz,
                "freq_delta_khz": round(f_angel_khz - f_demon_khz, 3),
                "zone_status": zone_status,
                "decay_type": decay_type,
                "protocol": protocol,
                "spatial_target": spatial
            })
        return matrix

    def execute_full_sweep(self, industry: str, payload: str, cycle: int) -> list:
        pool = SandboxManagerPool(industry=industry, count=10)
        offset = (cycle % 7) * 10
        total_master = len(self.master_matrix)

        def worker(idx):
            match = self.master_matrix[(offset + idx) % total_master]
            
            f_degree = match["midpoint_frequency_khz"]
            f_demon = match["f_demon_khz"]
            f_angel = match["f_angel_khz"]
            freq_delta = match["freq_delta_khz"]

            # Dynamic Velocities
            current_decay_speed = round(0.666 + (idx * 0.012) + ((cycle % 10) * 0.002), 4)
            current_restore_speed = round(0.710 + (idx * 0.022), 4)
            gap_to_unity = round(1.000 - current_restore_speed, 4)

            # Distance to 90-100 kHz Ultra Green Patch
            target_ultra_green = 95.0
            shift_required_khz = round(target_ultra_green - f_demon, 3)

            # Applied Vector Controls for Earth Deployment
            applied_speed_multiplier = round((f_angel / max(f_demon, 0.001)) * gap_to_unity, 4)
            bandwidth_spread_khz = round(freq_delta * self.PHI, 3)

            # Foreseen Failure Target Date
            pred_year = 2026 + (idx * 7) + (cycle % 11)
            pred_date = f"{pred_year}-{(idx%12)+1:02d}-{(cycle%28)+1:02d}"

            prompt = (
                f"Agent [{idx+1}/10] | Node: {payload}\n"
                f"Zodiac Sign: {match['zodiac_sign']} ({match['zodiac_band_range']})\n"
                f"Base Degree Frequency: {f_degree} kHz\n"
                f"Demon: {match['demon']} ({f_demon} kHz) | Angel: {match['angel']} ({f_angel} kHz)\n"
                f"Current Zone: {match['zone_status']}\n"
                f"Required Shift to Ultra Green (90-100 kHz): +{shift_required_khz} kHz\n"
                f"Applied Speed Required: {applied_speed_multiplier}x | Bandwidth Width: {bandwidth_spread_khz} kHz\n"
                f"Spatial Location: {match['spatial_target']}\n"
                f"Foreseen Peak Failure Date: {pred_date}\n"
            )

            try:
                raw = self.router.query(self.SYSTEM_PROMPT, prompt)
                data = json.loads(raw)
            except Exception:
                data = {
                    "agent_index": idx + 1,
                    "target_node_summary": payload[:60] + "...",
                    "space_time_curvature_status": {
                        "zodiac_sign": match["zodiac_sign"],
                        "base_degree_frequency_khz": f"{f_degree} kHz",
                        "zone_classification": match["zone_status"],
                        "ultra_green_patch_target": "90.0 kHz - 100.0 kHz"
                    },
                    "demon_resonance": {
                        "name": match["demon"],
                        "frequency_khz": f"{f_demon} kHz",
                        "decay_velocity": current_decay_speed,
                        "destabilization_floor": 0.666,
                        "foreseen_failure_date": pred_date
                    },
                    "angel_resonance": {
                        "name": match["angel"],
                        "choir": match["choir"],
                        "frequency_khz": f"{f_angel} kHz",
                        "current_restoration_speed": current_restore_speed,
                        "target_unity": 1.000
                    },
                    "real_time_earth_vector": {
                        "applied_speed": f"{applied_speed_multiplier}x acceleration",
                        "application_width_khz": f"{bandwidth_spread_khz} kHz bandwidth",
                        "frequency_shift_to_ultra_green": f"+{shift_required_khz} kHz shift",
                        "exact_spatial_target": match["spatial_target"]
                    },
                    "adjuration_protocol_directive": (
                        f"Inject {f_angel} kHz tone phase-locked across {bandwidth_spread_khz} kHz width at {match['spatial_target']} "
                        f"to shift node out of {match['zone_status']} into the 90-100 kHz Ultra Green Patch. "
                        f"Neutralizes {match['demon']} ({f_demon} kHz) at {applied_speed_multiplier}x speed before {pred_date}."
                    )
                }

            return {
                "sandbox_id": f"sentinel-c{idx+1:02d}",
                "status": "EXECUTED",
                "data": data
            }

        with ThreadPoolExecutor(max_workers=10) as executor:
            outputs = list(executor.map(worker, range(10)))

        return outputs
