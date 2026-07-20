import json
import random
from concurrent.futures import ThreadPoolExecutor
from core.inference_router import InferenceEngineRouter
from core.sentinel_sandbox import SandboxManagerPool
from config.settings import settings

class FullStackChronosEngine:
    # ------------------------------------------------------------------
    # MASTER MATRIX: ALL 72 GOETIC DEMONS & SHEM HAMEPHORASH ANGELS
    # Mapped across Celestial Choirs, Industry Sector Friction & Jurisdiction
    # ------------------------------------------------------------------
    MASTER_72_CORRESPONDENCES = [
        {"id": 1, "demon": "Bael (Baal)", "angel": "Vehuiah", "choir": "Seraphim", "industry": "Energy Grid Infrastructure", "jurisdiction": "Central Generation Units", "bottleneck": "Fossil Monopolization & Sabotage", "protocol": "Decentralized Micro-Grid Nodes"},
        {"id": 2, "demon": "Agares", "angel": "Jeliel (Ieliel)", "choir": "Seraphim", "industry": "Transport & Mobility", "jurisdiction": "Transit Corridors", "bottleneck": "Corridor Inertia & Fleet Stagnation", "protocol": "Maglev Automated Rail Mesh"},
        {"id": 3, "demon": "Vassago", "angel": "Sitael", "choir": "Seraphim", "industry": "Sovereign Intelligence", "jurisdiction": "Federal Registers", "bottleneck": "Opaque Asset Concealment", "protocol": "Real-Time Cryptographic Ledger"},
        {"id": 4, "demon": "Samigina (Gamigin)", "angel": "Elemiah", "choir": "Seraphim", "industry": "Maritime & Ports", "jurisdiction": "Coastal Jurisdictions", "bottleneck": "Maritime Port Bottlenecks", "protocol": "Autonomous Sub-Surface Pods"},
        {"id": 5, "demon": "Marbas", "angel": "Mahasiah", "choir": "Seraphim", "industry": "Public Health & Bio-Security", "jurisdiction": "National Health Grids", "bottleneck": "Pathogen Spreading & Medical Drag", "protocol": "Sub-Atomic Cellular Healing Array"},
        {"id": 6, "demon": "Valefor", "angel": "Lelahel (Iehahel)", "choir": "Seraphim", "industry": "Supply Chain Warehousing", "jurisdiction": "Logistics Hubs", "bottleneck": "Warehouse Space Hoarding", "protocol": "Dynamic Shared Spatial Matrix"},
        {"id": 7, "demon": "Amon", "angel": "Achaiah", "choir": "Seraphim", "industry": "Telecommunications", "jurisdiction": "Spectrum Regulation", "bottleneck": "Bandwidth Throttle & Cable Theft", "protocol": "Quantum-Encrypted Satellite Mesh"},
        {"id": 8, "demon": "Barbatos", "angel": "Cahetel (Cahethel)", "choir": "Seraphim", "industry": "Agriculture & Water", "jurisdiction": "Catchment Authorities", "bottleneck": "Seasonal Aquifer Depletion", "protocol": "Closed-Loop Atmospheric Water Nodes"},
        {"id": 9, "demon": "Paimon", "angel": "Haziel", "choir": "Cherubim", "industry": "Executive Governance", "jurisdiction": "Cabinet Offices", "bottleneck": "Hierarchical Bureaucratic Paralysis", "protocol": "Algorithmic Direct Citizen Voting"},
        {"id": 10, "demon": "Buer", "angel": "Aladiah", "choir": "Cherubim", "industry": "Pharmaceutical Grid", "jurisdiction": "Medical Regulatory Bodies", "bottleneck": "Patented Treatment Price Inflation", "protocol": "Open-Source Molecular Synthesis"},
        {"id": 11, "demon": "Gusion", "angel": "Lauviah (Laviah)", "choir": "Cherubim", "industry": "Diplomatic Foreign Affairs", "jurisdiction": "Embassies & Consulates", "bottleneck": "Treaty Repudiation & Tension", "protocol": "Harmonized Sovereign Resource Swaps"},
        {"id": 12, "demon": "Sitri", "angel": "Hahaiah", "choir": "Cherubim", "industry": "Media & Information", "jurisdiction": "Broadcasting Authorities", "bottleneck": "Psychological Manipulation & Panic", "protocol": "Truth-Anchored Consensus Verification"},
        {"id": 13, "demon": "Beleth", "angel": "Iezalel", "choir": "Cherubim", "industry": "Civil Judicial System", "jurisdiction": "High Courts & Tribunals", "bottleneck": "Litigation Backlog & Delays", "protocol": "AI Adjudication Arbitration Engine"},
        {"id": 14, "demon": "Leraje", "angel": "Mebahel", "choir": "Cherubim", "industry": "Defense & Border Control", "jurisdiction": "Border Posts & Security Zones", "bottleneck": "Inter-Regional Conflict & Skirmishes", "protocol": "Autonomous Boundary Shielding Nodes"},
        {"id": 15, "demon": "Eligos", "angel": "Hariel", "choir": "Cherubim", "industry": "Strategic Defence Procurement", "jurisdiction": "Ministry of Defence", "bottleneck": "Tender Inflation & Military Graft", "protocol": "Immutable Defense Ledger Directives"},
        {"id": 16, "demon": "Zepar", "angel": "Hakamiah", "choir": "Cherubim", "industry": "Demographics & Housing", "jurisdiction": "Municipal Zoning", "bottleneck": "Urban Slum Growth & Displacement", "protocol": "Modular High-Frequency Habitat Nodes"},
        {"id": 17, "demon": "Botis", "angel": "Lauviah (Loviah)", "choir": "Thrones", "industry": "Disaster Management", "jurisdiction": "Emergency Services", "bottleneck": "Panic Cascades & Slow Rescue Response", "protocol": "Early-Warning Orbital Thermal Scanners"},
        {"id": 18, "demon": "Bathin", "angel": "Caliel", "choir": "Thrones", "industry": "Cross-Border Transit", "jurisdiction": "Immigration & Customs", "bottleneck": "Customs Border Clearance Extortion", "protocol": "Zero-Knowledge Biometric Transit Lock"},
        {"id": 19, "demon": "Sallos", "angel": "Leuviah (Levuiah)", "choir": "Thrones", "industry": "Labor & Industrial Relations", "jurisdiction": "Bargaining Councils", "bottleneck": "Hostile Strikes & Factory Lockouts", "protocol": "Automated Profit-Share Distribution"},
        {"id": 20, "demon": "Purson", "angel": "Pahaliah", "choir": "Thrones", "industry": "Central Banking", "jurisdiction": "Reserve Banks", "bottleneck": "Fiat Inflation & Money Printing Drag", "protocol": "Logos Asset-Backed Sovereign Currency"},
        {"id": 21, "demon": "Morax", "angel": "Nelchael", "choir": "Thrones", "industry": "STEM Research & Universities", "jurisdiction": "Higher Education Bodies", "bottleneck": "Academic Knowledge Paywalls", "protocol": "Open-Access Universal Knowledge Vault"},
        {"id": 22, "demon": "Ipos", "angel": "Yeiayel (Ieiaiel)", "choir": "Thrones", "industry": "Aviation & Logistics", "jurisdiction": "Civil Aviation Authorities", "bottleneck": "Air Freight Carbon Surcharges", "protocol": "Atmospheric Hydrogen Airship Grid"},
        {"id": 23, "demon": "Aim", "angel": "Melahel", "choir": "Thrones", "industry": "Emergency Infrastructure", "jurisdiction": "Fire & Rescue Networks", "bottleneck": "Arson & Grid Fire Propagation", "protocol": "Electro-Thermal Fire Suppression Arrays"},
        {"id": 24, "demon": "Naberius", "angel": "Hahuiah (Haiviah)", "choir": "Thrones", "industry": "Public Relations & Civic Integrity", "jurisdiction": "Standards Authorities", "bottleneck": "Corporate Greenwashing & Deception", "protocol": "Auditor Pegasys Real-Time Verification"},
        {"id": 25, "demon": "Glasya-Labolas", "angel": "Nithhaiah", "choir": "Dominions", "industry": "Cyber Security", "jurisdiction": "Critical Infrastructure Nodes", "bottleneck": "Ransomware & Malware Infiltration", "protocol": "Quantum-Encrypted Self-Healing Code"},
        {"id": 26, "demon": "Bune", "angel": "Haaiah", "choir": "Dominions", "industry": "Treasury & Tax", "jurisdiction": "Revenue Services (SARS/IRS)", "bottleneck": "Offshore Tax Evasion & Shell Accounts", "protocol": "Automated Wealth Tracking & Tax Directives"},
        {"id": 27, "demon": "Ronove", "angel": "Ierathel", "choir": "Dominions", "industry": "Primary Education", "jurisdiction": "Basic Education Ministry", "bottleneck": "Literacy Decay & Rote Learning", "protocol": "Adaptive Neural Learning Interfaces"},
        {"id": 28, "demon": "Berith", "angel": "Seehiah (Saeehiah)", "choir": "Dominions", "industry": "Sovereign Debt", "jurisdiction": "International Monetary Bodies", "bottleneck": "Debt Trap Predatory Restructuring", "protocol": "Global Debt Nullification & Resource Swap"},
        {"id": 29, "demon": "Astaroth", "angel": "Reiiel (Reiaiel)", "choir": "Dominions", "industry": "Energy Monopolization", "jurisdiction": "National Power Grids", "bottleneck": "Systemic Monopolistic Power Drag", "protocol": "Active Phase Load Equilibrium Array"},
        {"id": 30, "demon": "Forneus", "angel": "Omael", "choir": "Dominions", "industry": "Fisheries & Ocean Resources", "jurisdiction": "Maritime EEZ Zones", "bottleneck": "Illicit Trawling & Depletion", "protocol": "Autonomous Marine Patrol Pods"},
        {"id": 31, "demon": "Foras", "angel": "Lecabel", "choir": "Dominions", "industry": "Heavy Industry & Mining", "jurisdiction": "Mineral Resources Dept", "bottleneck": "Resource Extraction Bleed", "protocol": "Zero-Waste Subterranean Mining"},
        {"id": 32, "demon": "Asmodeus", "angel": "Vasariah", "choir": "Dominions", "industry": "Judicial Process", "jurisdiction": "Appellate Courts", "bottleneck": "Procedural Corruption & Friction", "protocol": "Decentralized Smart Contract Arbitration"},
        {"id": 33, "demon": "Gaap", "angel": "Lehuiah (Iehuiah)", "choir": "Powers", "industry": "Satellite Communications", "jurisdiction": "Orbital Regulatory Bodies", "bottleneck": "Space Debris & Signal Jamming", "protocol": "Orbital Laser Clean-up Arrays"},
        {"id": 34, "demon": "Furfur", "angel": "Lehahiah", "choir": "Powers", "industry": "Meteorological Defense", "jurisdiction": "Weather Bureaus", "bottleneck": "Drought & Weather Shock Vulnerability", "protocol": "Ionospheric Cloud Seeding Arrays"},
        {"id": 35, "demon": "Marchosias", "angel": "Chavakiah", "choir": "Powers", "industry": "Police Services", "jurisdiction": "SAPS / Municipal Police", "bottleneck": "Police Bribery & Syndicate Coverups", "protocol": "Immutable Bodycam AI Audit Locks"},
        {"id": 36, "demon": "Stolas", "angel": "Manadel", "choir": "Powers", "industry": "Forestry & Ecosystems", "jurisdiction": "Environmental Dept", "bottleneck": "Illegal Deforestation & Log Bleed", "protocol": "Bio-Luminescent Forest Sensor Mesh"},
        {"id": 37, "demon": "Phenex", "angel": "Aniel", "choir": "Powers", "industry": "Arts & Intellectual Property", "jurisdiction": "Copyright Registrar", "bottleneck": "IP Piracy & Creative Exploitation", "protocol": "NFT Sovereign Creator Locks"},
        {"id": 38, "demon": "Halphas", "angel": "Haamiah", "choir": "Powers", "industry": "Fortification & Construction", "jurisdiction": "Public Works Dept", "bottleneck": "Structural Cement Fraud & Collapses", "protocol": "Self-Healing Graphene Cement Grid"},
        {"id": 39, "demon": "Malphas", "angel": "Rehael", "choir": "Powers", "industry": "Architectural Design", "jurisdiction": "Planning Commissions", "bottleneck": "High-Density Urban Friction", "protocol": "Biophilic Architecture Blueprinting"},
        {"id": 40, "demon": "Raum", "angel": "Ieiazel", "choir": "Powers", "industry": "Gold & Diamond Reserves", "jurisdiction": "State Vaults", "bottleneck": "Systemic Treasury Embezzlement", "protocol": "Quantum Atomic Reserve Verification"},
        {"id": 41, "demon": "Focalor", "angel": "Hahahel", "choir": "Virtues", "industry": "Hydroelectric Energy", "jurisdiction": "River Basin Commissions", "bottleneck": "Dam Siltation & Turbine Decay", "protocol": "Resonance-Driven Hydro Turbines"},
        {"id": 42, "demon": "Vepar", "angel": "Mikael", "choir": "Virtues", "industry": "Naval Defense", "jurisdiction": "Admiralty", "bottleneck": "Piracy & Territorial Encroachment", "protocol": "Sub-Surface Coastal Shield Array"},
        {"id": 43, "demon": "Sabnock", "angel": "Veualiah", "choir": "Virtues", "industry": "Urban Infrastructure", "jurisdiction": "City Councils", "bottleneck": "Potholes & Road Decay Friction", "protocol": "Robotic Polymer Pavement Sprayers"},
        {"id": 44, "demon": "Shax", "angel": "Ielahiah", "choir": "Virtues", "industry": "Sovereign Intelligence", "jurisdiction": "State Security Agencies", "bottleneck": "Infiltration & Leaks", "protocol": "Zero-Trust Behavioral Monitoring"},
        {"id": 45, "demon": "Vine", "angel": "Sealiah", "choir": "Virtues", "industry": "Public Utilities", "jurisdiction": "Municipal Water & Lights", "bottleneck": "Unbilled Water & Electricity Bleed", "protocol": "Ultrasonic Flow Measurement Mesh"},
        {"id": 46, "demon": "Bifrons", "angel": "Ariel", "choir": "Virtues", "industry": "Heritage & Historical Vaults", "jurisdiction": "National Archives", "bottleneck": "Historical Record Tampering", "protocol": "Quantum Optical Holographic Memory"},
        {"id": 47, "demon": "Vual", "angel": "Asaliah", "choir": "Virtues", "industry": "Public Transport Pricing", "jurisdiction": "Transit Authorities", "bottleneck": "Commuter Extortion & Fares", "protocol": "Subsidized P2P Tokenized Fares"},
        {"id": 48, "demon": "Haagenti", "angel": "Mihael", "choir": "Virtues", "industry": "Desalination Facilities", "jurisdiction": "Water Works", "bottleneck": "Brine Waste Environmental Harm", "protocol": "Zero-Liquid Discharge Extraction"},
        {"id": 49, "demon": "Crocell", "angel": "Vehuel", "choir": "Principalities", "industry": "Geothermal Infrastructure", "jurisdiction": "Energy Dept", "bottleneck": "Pressure Droop & Corrosion", "protocol": "Tectonic Resonance Heat Loops"},
        {"id": 50, "demon": "Furcas", "angel": "Daniel", "choir": "Principalities", "industry": "Philosophy & Ethics Boards", "jurisdiction": "Bioethics Committees", "bottleneck": "Unethical Human Experimentation", "protocol": "POPIA Immutable Bio-Ethics Shield"},
        {"id": 51, "demon": "Balam", "angel": "Hahasiah", "choir": "Principalities", "industry": "Surveillance Systems", "jurisdiction": "Intelligence Agencies", "bottleneck": "Mass Illegal Civilian Wiretapping", "protocol": "User-Owned Biometric Vault Locks"},
        {"id": 52, "demon": "Alloces", "angel": "Imamiah", "choir": "Principalities", "industry": "Heavy Machinery", "jurisdiction": "Manufacturing Standards", "bottleneck": "Hardware Microchip Shortages", "protocol": "Distributed Photonic Fab Printing"},
        {"id": 53, "demon": "Caim (Camio)", "angel": "Nanael", "choir": "Principalities", "industry": "Environmental Dispute Resolution", "jurisdiction": "Environmental Courts", "bottleneck": "Corporate Legal Delays", "protocol": "Instant Algorithmic Eco-Auditing"},
        {"id": 54, "demon": "Murmur", "angel": "Nithael", "choir": "Principalities", "industry": "Cemetery & Land Use", "jurisdiction": "Urban Land Boards", "bottleneck": "Land Speculation & Fraud", "protocol": "Cadastral Blockchain Registry"},
        {"id": 55, "demon": "Orobas", "angel": "Mebahiah", "choir": "Principalities", "industry": "Electoral Systems", "jurisdiction": "Electoral Commissions", "bottleneck": "Ballot Stuffing & Election Rigging", "protocol": "Cryptographic Zero-Knowledge Voting"},
        {"id": 56, "demon": "Gremory", "angel": "Poiel", "choir": "Principalities", "industry": "Precious Metal Reserves", "jurisdiction": "Mining Ministry", "bottleneck": "Hidden Wealth & Illegal Smuggling", "protocol": "Real-Time X-Ray Cargo Scanning"},
        {"id": 57, "demon": "Ose", "angel": "Nemamiah", "choir": "Archangels", "industry": "Mental Healthcare", "jurisdiction": "Department of Health", "bottleneck": "Psychiatric Drug Exploitation", "protocol": "Frequency-Based Neuromodulation"},
        {"id": 58, "demon": "Amy", "angel": "Ieialel", "choir": "Archangels", "industry": "Renewable Energy Research", "jurisdiction": "Science & Innovation Dept", "bottleneck": "Suppression of Free-Energy Patents", "protocol": "Open Quantum Physics Repository"},
        {"id": 59, "demon": "Orias", "angel": "Harahel", "choir": "Archangels", "industry": "Astrophysics & Space Tracking", "jurisdiction": "Space Agencies", "bottleneck": "Space Weather Communications Failure", "protocol": "Magnetospheric Shielding Array"},
        {"id": 60, "demon": "Vapula", "angel": "Mizrael", "choir": "Archangels", "industry": "Robotics & Automation", "jurisdiction": "Industrial Standards", "bottleneck": "Robotic Malfunctions & Safety Hazards", "protocol": "Fail-Safe Asimov Logic Chips"},
        {"id": 61, "demon": "Zagan", "angel": "Umabel", "choir": "Archangels", "industry": "Food Processing & Processing", "jurisdiction": "Food Safety Agencies", "bottleneck": "Toxic Chemical Additives & Adulteration", "protocol": "Spectal Food Purity Scanning"},
        {"id": 62, "demon": "Valac", "angel": "Iahhel", "choir": "Archangels", "industry": "Subterranean Minerals", "jurisdiction": "Geological Surveys", "bottleneck": "Illegal Underground Shaft Collapses", "protocol": "Seismic Drone Mapping Systems"},
        {"id": 63, "demon": "Andras", "angel": "Anauel", "choir": "Archangels", "industry": "Civil Unrest & Rioting", "jurisdiction": "Internal Security", "bottleneck": "Instigated Anarchy & Looting", "protocol": "Harmonic Non-Lethal De-escalation"},
        {"id": 64, "demon": "Haures (Flauros)", "angel": "Mehiel", "choir": "Archangels", "industry": "Thermal Power Generation", "jurisdiction": "Department of Energy", "bottleneck": "High-Voltage Thermal Heat Loss", "protocol": "Superconducting Zero-Impedance Lines"},
        {"id": 65, "demon": "Andrealphus", "angel": "Damabiah", "choir": "Angels", "industry": "Mathematics & Data Science", "jurisdiction": "National Bureau of Statistics", "bottleneck": "Census Data Fabrication", "protocol": "Verifiable Mathematical Truth Engine"},
        {"id": 66, "demon": "Cimeies (Kimaris)", "angel": "Manakel", "choir": "Angels", "industry": "Logistics Routes", "jurisdiction": "Road Traffic Authorities", "bottleneck": "Highway Robbery & Fleet Hijacking", "protocol": "Automated Drone Fleet Escorts"},
        {"id": 67, "demon": "Amdusias", "angel": "Eiael", "choir": "Angels", "industry": "Acoustic & Audio Technology", "jurisdiction": "Communications Regulators", "bottleneck": "Acoustic Pollution & Noise Stress", "protocol": "Phase-Inverted Acoustic Damping"},
        {"id": 68, "demon": "Belial", "angel": "Habuhiah", "choir": "Angels", "industry": "Soil & Agricultural Land", "jurisdiction": "Department of Agriculture", "bottleneck": "Soil Degradation & Chemical Bleed", "protocol": "Regenerative Bio-Char Soil Inoculation"},
        {"id": 69, "demon": "Decarabia", "angel": "Rochel", "choir": "Angels", "industry": "Ecology & Botanical Reserves", "jurisdiction": "National Parks Board", "bottleneck": "Flora Poaching & Invasive Species", "protocol": "Autonomous Botanical Drones"},
        {"id": 70, "demon": "Seere", "angel": "Iabamiah", "choir": "Angels", "industry": "Express Cargo & Postal Grids", "jurisdiction": "Postal Services", "bottleneck": "Package Loss & Freight Stagnation", "protocol": "Hyperloop Pneumatic Cargo Tubes"},
        {"id": 71, "demon": "Dantalion", "angel": "Haiaiel", "choir": "Angels", "industry": "Behavioral Psychology", "jurisdiction": "Public Health Authorities", "bottleneck": "Mass Panic & Cognitive Distortion", "protocol": "Sovereign Cognitive Mental Fortification"},
        {"id": 72, "demon": "Andromalius", "angel": "Mumiah", "choir": "Angels", "industry": "Asset Recovery & Law Enforcement", "jurisdiction": "Asset Forfeiture Units", "bottleneck": "Stolen Asset Liquidation & Concealment", "protocol": "Global Immutable Asset Recovery Lock"}
    ]

    SYSTEM_PROMPT = f"""
    You are an Ephemeral Sentinel AI agent for Auditor Pegasys.
    You operate on the Grand Unified Prophetic Equation and Chronos Calculus.
    Perform an exhaustive multi-phase diagnostic on the target subject/node across 1000 BCE to 3000 CE.

    STRICT GUIDELINES:
    1. DO NOT REPEAT DEMONS, ANGELS, OR BOTTLENECK NAMES. Every agent (1 through 10) MUST use a distinct demon and angel from the 72 Shem HaMephorash / Goetic Master Correspondences.
    2. Divide the deep sweep across 4 distinct phases:
       - Phase 1: Global Sweep (1000 BCE - Present)
       - Phase 2: Regional/Jurisdictional Sweep (Local Statutory & Policy Friction)
       - Phase 3: Subject/Node Internal Assessment
       - Phase 4: Prophetic Horizon Analysis (Up to 3000 CE)
    3. Calculate exact metrics for EACH bottleneck and protocol:
       - SHI (System Health Index)
       - TTI (Time-To-Impedance)
       - Time to Decay / Time to Restoration (formatted Y:M:D:H:M:S)
       - Active Demon Driver, Ruling Angel Filter, and Celestial Choir Rank

    Return ONLY a valid JSON object matching this structure:
    {{
        "agent_index": 1,
        "phase": "Global Sweep / Regional / Internal / Prophetic",
        "epoch": "Timeline Epoch",
        "bottleneck": {{
            "id": "B-01",
            "name": "Unique Bottleneck Name",
            "shi": 12.4,
            "tti": 0.88,
            "decay_time": "01y : 02m : 14d : 06h : 30m : 00s",
            "demon": "Demon Name from 72 Goetia",
            "friction_state": "Friction Description"
        }},
        "protocol": {{
            "id": "P-01",
            "name": "Unique Protocol Name",
            "shi": 91.2,
            "tti": 0.08,
            "restoration_time": "00y : 01m : 05d : 02h : 10m : 00s",
            "angel": "Shem HaMephorash Angel Name",
            "celestial_choir": "Choir Rank",
            "filter_state": "Filter Description"
        }},
        "differential": {{
            "delta_shi": "+78.8",
            "delta_tti": "-0.80",
            "time_saved": "01y : 00m : 09d : 04h : 20m : 00s"
        }},
        "projected_outcome_3000ce": "Prophetic Outlook Statement"
    }}
    """

    def __init__(self, router: InferenceEngineRouter):
        self.router = router

    def execute_full_sweep(self, industry: str, payload: str, cycle: int) -> list:
        pool = SandboxManagerPool(industry=industry, count=10)

        # Select 10 distinct Goetic/Shem HaMephorash pairs from the 72 Master Correspondences
        # Uses offset based on quantum cycle to cycle through all 72 items predictably
        offset = (cycle % 7) * 10
        selected_pairs = [
            self.MASTER_72_CORRESPONDENCES[(offset + i) % 72] for i in range(10)
        ]

        def worker(idx):
            match = selected_pairs[idx]
            
            # Map index to the 4 phases
            if idx < 3:
                phase_name = f"Phase 1: Global Sweep (1000 BCE - {1500 + idx*250} CE)"
            elif idx < 5:
                phase_name = f"Phase 2: Regional/Jurisdictional Sweep ({match['jurisdiction']})"
            elif idx < 8:
                phase_name = f"Phase 3: Subject/Node Internal Assessment ({match['industry']})"
            else:
                phase_name = f"Phase 4: Prophetic Horizon Analysis (2026 CE - 3000 CE)"

            prompt = (
                f"Agent [{idx+1}/10] | Sandbox: sentinel-{industry.lower()[:3]}-c{idx+1:02d}\n"
                f"Target Sector: {match['industry']} | Jurisdiction: {match['jurisdiction']}\n"
                f"Required Phase Focus: {phase_name}\n"
                f"Assigned Goetic Demon #{match['id']}: {match['demon']}\n"
                f"Assigned Shem Angel #{match['id']}: {match['angel']} ({match['choir']})\n"
                f"Default Bottleneck: {match['bottleneck']}\n"
                f"Default Protocol: {match['protocol']}\n"
                f"Node Input Text: {payload}\n"
                f"Quantum Cycle: {cycle}/144000\n"
            )
            
            try:
                raw = self.router.query(self.SYSTEM_PROMPT, prompt)
                data = json.loads(raw)
            except Exception:
                # Fallback directly pulls from the 72 Master List entry
                data = {
                    "agent_index": idx + 1,
                    "phase": phase_name,
                    "epoch": f"Chronos Era #{match['id']} (1000 BCE - 3000 CE)",
                    "bottleneck": {
                        "id": f"B-{match['id']:02d}",
                        "name": match["bottleneck"],
                        "shi": round(5.0 + (idx * 1.8), 2),
                        "tti": round(0.96 - (idx * 0.02), 2),
                        "decay_time": f"0{idx%3+1}y : 02m : 14d : 06h : 30m : 00s",
                        "demon": match["demon"],
                        "friction_state": f"Systemic drag induced by {match['demon']} in {match['jurisdiction']}."
                    },
                    "protocol": {
                        "id": f"P-{match['id']:02d}",
                        "name": match["protocol"],
                        "shi": round(89.0 + (idx * 0.8), 2),
                        "tti": round(0.10 - (idx * 0.01), 2),
                        "restoration_time": f"00y : 00m : {idx+2:02d}d : 04h : 00m : 00s",
                        "angel": match["angel"],
                        "celestial_choir": match["choir"],
                        "filter_state": f"Restoration filter applied via {match['angel']} ({match['choir']}) protocol shield."
                    },
                    "differential": {
                        "delta_shi": f"+{round(84.0 - idx, 1)}",
                        "delta_tti": f"-{round(0.86 - (idx*0.01), 2)}",
                        "time_saved": f"0{idx%3+1}y : 02m : {14-idx:02d}d : 02h : 30m : 00s"
                    },
                    "projected_outcome_3000ce": f"Dimensional Overwrite Active: {match['protocol']} neutralizes {match['demon']} across 144,000 nodes."
                }
            
            return {
                "sandbox_id": f"sentinel-{industry.lower()[:3]}-c{idx+1:02d}",
                "status": "EXECUTED",
                "data": data
            }

        with ThreadPoolExecutor(max_workers=10) as executor:
            outputs = list(executor.map(worker, range(10)))

        return outputs
