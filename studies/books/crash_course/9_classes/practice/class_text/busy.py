#!/usr/bin/env python
import os, sys
sys.path.insert(0,'./import')
from scroll_text import TextScroll

def main():


	text_var_1 = """
[    0.000000] random: get_random_bytes called from start_kernel+0x42/0x50d with crng_init=0
[    0.000000] Linux version 4.13.0-36-generic (buildd@lgw01-amd64-033) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.9)) #40~16.04.1-Ubuntu SMP Fri Feb 16 23:25:58 UTC 2018 (Ubuntu 4.13.0-36.40~16.04.1-generic 4.13.13)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-36-generic.efi.signed root=UUID=c6b9b4d6-4292-4129-9a38-b57109cac95d ro quiet splash vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x008: 'MPX bounds registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x010: 'MPX CSR'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: xstate_offset[3]:  832, xstate_sizes[3]:   64
[    0.000000] x86/fpu: xstate_offset[4]:  896, xstate_sizes[4]:   64
[    0.000000] x86/fpu: Enabled xstate features 0x1f, context size is 960 bytes, using 'compacted' format.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000057fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000058000-0x0000000000058fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000059000-0x000000000009dfff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009e000-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000825b3fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000825b4000-0x00000000825b4fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000825b5000-0x00000000825defff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000825df000-0x000000008519dfff] usable
[    0.000000] BIOS-e820: [mem 0x000000008519e000-0x0000000085e79fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000085e7a000-0x0000000086514fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000086515000-0x00000000870a4fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000870a5000-0x0000000087efffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000087f00000-0x0000000087f7efff] type 20
[    0.000000] BIOS-e820: [mem 0x0000000087f7f000-0x0000000087ffefff] usable
[    0.000000] BIOS-e820: [mem 0x0000000088000000-0x00000000880fffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000e0000000-0x00000000efffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fe000000-0x00000000fe010fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x0000000471ffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] efi: EFI v2.40 by American Megatrends
[    0.000000] efi:  ESRT=0x87e47e18  ACPI=0x86619000  ACPI 2.0=0x86619000  SMBIOS=0x87661000  SMBIOS 3.0=0x87660000 
[    0.000000] random: fast init done
[    0.000000] SMBIOS 3.0.0 present.
[    0.000000] DMI: ASUSTeK COMPUTER INC. UX310UA/UX310UA, BIOS UX310UA.202 05/18/2016
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x472000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: write-back
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 00C0000000 mask 7FC0000000 uncachable
[    0.000000]   1 base 00A0000000 mask 7FE0000000 uncachable
[    0.000000]   2 base 0090000000 mask 7FF0000000 uncachable
[    0.000000]   3 base 008C000000 mask 7FFC000000 uncachable
[    0.000000]   4 base 008A000000 mask 7FFE000000 uncachable
[    0.000000]   5 base 0089000000 mask 7FFF000000 uncachable
[    0.000000]   6 base 0088800000 mask 7FFF800000 uncachable
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WC  UC- WT  
[    0.000000] e820: last_pfn = 0x87fff max_arch_pfn = 0x400000000
[    0.000000] esrt: Reserving ESRT space from 0x0000000087e47e18 to 0x0000000087e47e50.
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [ffff8a1d80098000] 98000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x3e352a000, 0x3e352afff] PGTABLE
[    0.000000] BRK [0x3e352b000, 0x3e352bfff] PGTABLE
[    0.000000] BRK [0x3e352c000, 0x3e352cfff] PGTABLE
[    0.000000] BRK [0x3e352d000, 0x3e352dfff] PGTABLE
[    0.000000] BRK [0x3e352e000, 0x3e352efff] PGTABLE
[    0.000000] BRK [0x3e352f000, 0x3e352ffff] PGTABLE
[    0.000000] BRK [0x3e3530000, 0x3e3530fff] PGTABLE
[    0.000000] BRK [0x3e3531000, 0x3e3531fff] PGTABLE
[    0.000000] BRK [0x3e3532000, 0x3e3532fff] PGTABLE
[    0.000000] BRK [0x3e3533000, 0x3e3533fff] PGTABLE
[    0.000000] BRK [0x3e3534000, 0x3e3534fff] PGTABLE
[    0.000000] Secure boot could not be determined
[    0.000000] RAMDISK: [mem 0x321c6000-0x350dafff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x0000000086619000 000024 (v02 _ASUS_)
[    0.000000] ACPI: XSDT 0x00000000866190A0 0000C4 (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x000000008663EF50 00010C (v05 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: DSDT 0x00000000866191F8 025D56 (v02 _ASUS_ Notebook 01072009 INTL 20120913)
[    0.000000] ACPI: FACS 0x000000008708BF80 000040
[    0.000000] ACPI: APIC 0x000000008663F060 000084 (v03 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x000000008663F0E8 000044 (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: FIDT 0x000000008663F130 00009C (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: MCFG 0x000000008663F1D0 00003C (v01 _ASUS_ Notebook 01072009 MSFT 00000097)
[    0.000000] ACPI: HPET 0x000000008663F210 000038 (v01 _ASUS_ Notebook 01072009 AMI. 0005000B)
[    0.000000] ACPI: SSDT 0x000000008663F248 000315 (v01 SataRe SataTabl 00001000 INTL 20120913)
[    0.000000] ACPI: ECDT 0x000000008663F560 0000C1 (v01 _ASUS_ Notebook 01072009 AMI. 00000005)
[    0.000000] ACPI: LPIT 0x000000008663F628 000094 (v01 INTEL  SKL-ULT  00000000 MSFT 0000005F)
[    0.000000] ACPI: SSDT 0x000000008663F6C0 000248 (v02 INTEL  sensrhub 00000000 INTL 20120913)
[    0.000000] ACPI: DBGP 0x000000008663F908 000034 (v01 INTEL           00000000 MSFT 0000005F)
[    0.000000] ACPI: DBG2 0x000000008663F940 000054 (v00 INTEL           00000000 MSFT 0000005F)
[    0.000000] ACPI: SSDT 0x000000008663F998 003F2E (v02 DptfTa DptfTabl 00001000 INTL 20120913)
[    0.000000] ACPI: SSDT 0x00000000866438C8 005846 (v02 SaSsdt SaSsdt   00003000 INTL 20120913)
[    0.000000] ACPI: UEFI 0x0000000086649110 000042 (v01                 00000000      00000000)
[    0.000000] ACPI: SSDT 0x0000000086649158 000E73 (v02 CpuRef CpuSsdt  00003000 INTL 20120913)
[    0.000000] ACPI: BGRT 0x0000000086649FD0 000038 (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: DMAR 0x000000008664A008 0000F0 (v01 INTEL  SKL      00000001 INTL 00000001)
[    0.000000] ACPI: TPM2 0x000000008664A0F8 000034 (v03        Tpm2Tabl 00000001 AMI  00000000)
[    0.000000] ACPI: MSDM 0x0000000085C3BF18 000055 (v03 _ASUS_ Notebook 00000000 ASUS 00000001)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x0000000471ffffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x471fd5000-0x471ffffff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x0000000471ffffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x0000000000057fff]
[    0.000000]   node   0: [mem 0x0000000000059000-0x000000000009dfff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x00000000825b3fff]
[    0.000000]   node   0: [mem 0x00000000825df000-0x000000008519dfff]
[    0.000000]   node   0: [mem 0x0000000085e7a000-0x0000000086514fff]
[    0.000000]   node   0: [mem 0x0000000087f7f000-0x0000000087ffefff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x0000000471ffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x0000000471ffffff]
[    0.000000] On node 0 totalpages: 4159530
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 22 pages reserved
[    0.000000]   DMA zone: 3996 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 8483 pages used for memmap
[    0.000000]   DMA32 zone: 542862 pages, LIFO batch:31
[    0.000000]   Normal zone: 56448 pages used for memmap
[    0.000000]   Normal zone: 3612672 pages, LIFO batch:31
[    0.000000] Reserving Intel graphics memory at 0x0000000089000000-0x000000008cffffff
[    0.000000] ACPI: PM-Timer IO Port: 0x1808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-119
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a701 base: 0xfed00000
[    0.000000] [Firmware Bug]: TSC_DEADLINE disabled due to Errata; please update microcode to version: 0xb2 (or later)
[    0.000000] smpboot: Allowing 4 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x00058000-0x00058fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009e000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x825b4000-0x825b4fff]
[    0.000000] PM: Registered nosave memory: [mem 0x825b5000-0x825defff]
[    0.000000] PM: Registered nosave memory: [mem 0x8519e000-0x85e79fff]
[    0.000000] PM: Registered nosave memory: [mem 0x86515000-0x870a4fff]
[    0.000000] PM: Registered nosave memory: [mem 0x870a5000-0x87efffff]
[    0.000000] PM: Registered nosave memory: [mem 0x87f00000-0x87f7efff]
[    0.000000] PM: Registered nosave memory: [mem 0x87fff000-0x87ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x88000000-0x880fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x88100000-0x88ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x89000000-0x8cffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x8d000000-0xdfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xe0000000-0xefffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf0000000-0xfdffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe000000-0xfe010fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe011000-0xfebfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec01000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0x8d000000-0xdfffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:4 nr_cpu_ids:4 nr_node_ids:1
[    0.000000] percpu: Embedded 45 pages/cpu @ffff8a21f1c00000 s146520 r8192 d29608 u524288
[    0.000000] pcpu-alloc: s146520 r8192 d29608 u524288 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1 2 3 
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 4094513
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-36-generic.efi.signed root=UUID=c6b9b4d6-4292-4129-9a38-b57109cac95d ro quiet splash vt.handoff=7
[    0.000000] PID hash table entries: 4096 (order: 3, 32768 bytes)
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 16176176K/16638120K available (12300K kernel code, 2481K rwdata, 4008K rodata, 2364K init, 2368K bss, 461944K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] Kernel/User page tables isolation: enabled
[    0.000000] ftrace: allocating 37831 entries in 148 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=4.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 524544, nr_irqs: 1024, preallocated irqs: 16
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635855245 ns
[    0.000000] hpet clockevent registered
[    0.004000] tsc: Detected 2600.000 MHz processor
[    0.004000] Calibrating delay loop (skipped), value calculated using timer frequency.. 5184.00 BogoMIPS (lpj=10368000)
[    0.004000] pid_max: default: 32768 minimum: 301
[    0.004000] ACPI: Core revision 20170531
[    0.042558] ACPI: 6 ACPI AML tables successfully acquired and loaded
[    0.043766] Security Framework initialized
[    0.043767] Yama: becoming mindful.
[    0.043783] AppArmor: AppArmor initialized
[    0.045974] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes)
[    0.047031] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.047070] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.047104] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.047278] CPU: Physical Processor ID: 0
[    0.047279] CPU: Processor Core ID: 0
[    0.047284] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.047284] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.047286] FEATURE SPEC_CTRL Not Present
[    0.047290] mce: CPU supports 8 MCE banks
[    0.047299] CPU0: Thermal monitoring enabled (TM1)
[    0.047314] process: using mwait in idle threads
[    0.047316] Last level iTLB entries: 4KB 64, 2MB 8, 4MB 8
[    0.047317] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    0.047318] Spectre V2 mitigation: Mitigation: Full generic retpoline
[    0.047319] Spectre V2 mitigation: Speculation control IBPB not-supported IBRS not-supported
[    0.047320] Spectre V2 mitigation: Filling RSB on context switch
[    0.047842] Freeing SMP alternatives memory: 36K
[    0.051156] smpboot: Max logical packages: 2
[    0.051163] DMAR: Host address width 39
[    0.051164] DMAR: DRHD base: 0x000000fed90000 flags: 0x0
[    0.051171] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap 1c0000c40660462 ecap 7e3ff0505e
[    0.051172] DMAR: DRHD base: 0x000000fed91000 flags: 0x1
[    0.051176] DMAR: dmar1: reg_base_addr fed91000 ver 1:0 cap d2008c40660462 ecap f050da
[    0.051177] DMAR: RMRR base: 0x00000085c1b000 end: 0x00000085c3afff
[    0.051179] DMAR: RMRR base: 0x00000088800000 end: 0x0000008cffffff
[    0.051180] DMAR: ANDD device: 1 name: \_SB.PCI0.I2C0
[    0.051180] DMAR: ANDD device: 2 name: \_SB.PCI0.I2C1
[    0.051182] DMAR-IR: IOAPIC id 2 under DRHD base  0xfed91000 IOMMU 1
[    0.051183] DMAR-IR: HPET id 0 under DRHD base 0xfed91000
[    0.051184] DMAR-IR: x2apic is disabled because BIOS sets x2apic opt out bit.
[    0.051184] DMAR-IR: Use 'intremap=no_x2apic_optout' to override the BIOS setting.
[    0.052649] DMAR-IR: Enabled IRQ remapping in xapic mode
[    0.052650] x2apic: IRQ remapping doesn't support X2APIC mode
[    0.056843] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.100000] smpboot: CPU0: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (family: 0x6, model: 0x4e, stepping: 0x3)
[    0.100000] Performance Events: PEBS fmt3+, Skylake events, 32-deep LBR, full-width counters, Intel PMU driver.
[    0.100000] ... version:                4
[    0.100000] ... bit width:              48
[    0.100000] ... generic registers:      4
[    0.100000] ... value mask:             0000ffffffffffff
[    0.100000] ... max period:             00007fffffffffff
[    0.100000] ... fixed-purpose events:   3
[    0.100000] ... event mask:             000000070000000f
[    0.100000] Hierarchical SRCU implementation.
[    0.100000] smp: Bringing up secondary CPUs ...
[    0.100000] x86: Booting SMP configuration:
[    0.100000] .... node  #0, CPUs:      #1
[    0.100000] NMI watchdog: enabled on all CPUs, permanently consumes one hw-PMU counter.
[    0.100000]  #2 #3
[    0.100000] smp: Brought up 1 node, 4 CPUs
[    0.100000] smpboot: Total of 4 processors activated (20736.00 BogoMIPS)
[    0.100400] devtmpfs: initialized
[    0.100400] x86/mm: Memory block size: 128MB
[    0.104855] evm: security.selinux
[    0.104856] evm: security.SMACK64
[    0.104856] evm: security.SMACK64EXEC
[    0.104856] evm: security.SMACK64TRANSMUTE
[    0.104857] evm: security.SMACK64MMAP
[    0.104858] evm: security.ima
[    0.104858] evm: security.capability
[    0.104871] PM: Registering ACPI NVS region [mem 0x825b4000-0x825b4fff] (4096 bytes)
[    0.104871] PM: Registering ACPI NVS region [mem 0x86515000-0x870a4fff] (12124160 bytes)
[    0.104871] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.104871] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.104871] pinctrl core: initialized pinctrl subsystem
[    0.104871] RTC time: 22:41:33, date: 02/24/18
[    0.104871] NET: Registered protocol family 16
[    0.104871] cpuidle: using governor ladder
[    0.104871] cpuidle: using governor menu
[    0.104871] PCCT header not found.
[    0.104871] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.104871] ACPI: bus type PCI registered
[    0.104871] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.104871] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0xe0000000-0xefffffff] (base 0xe0000000)
[    0.104871] PCI: MMCONFIG at [mem 0xe0000000-0xefffffff] reserved in E820
[    0.104871] PCI: Using configuration type 1 for base access
[    0.104871] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.104871] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.104871] ACPI: Added _OSI(Module Device)
[    0.104871] ACPI: Added _OSI(Processor Device)
[    0.104871] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.104871] ACPI: Added _OSI(Processor Aggregator Device)
[    0.104871] ACPI: EC: EC started
[    0.104871] ACPI: EC: interrupt blocked
[    0.109189] ACPI: \: Used as first EC
[    0.109191] ACPI: \: GPE=0x50, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.109192] ACPI: \: Used as boot ECDT EC to handle transactions
[    0.109978] ACPI: Executed 21 blocks of module-level executable AML code
[    0.122346] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.128728] ACPI: Dynamic OEM Table Load:
[    0.128748] ACPI: SSDT 0xFFFF8A21DED0D800 000660 (v02 PmRef  Cpu0Ist  00003000 INTL 20120913)
[    0.129129] ACPI: \_PR_.CPU0: _OSC native thermal LVT Acked
[    0.130616] ACPI: Dynamic OEM Table Load:
[    0.130621] ACPI: SSDT 0xFFFF8A21DED87000 00037F (v02 PmRef  Cpu0Cst  00003001 INTL 20120913)
[    0.130993] ACPI: Dynamic OEM Table Load:
[    0.130997] ACPI: SSDT 0xFFFF8A21DED26480 00008E (v02 PmRef  Cpu0Hwp  00003000 INTL 20120913)
[    0.131270] ACPI: Dynamic OEM Table Load:
[    0.131274] ACPI: SSDT 0xFFFF8A21DEDB8C00 000130 (v02 PmRef  HwpLvt   00003000 INTL 20120913)
[    0.132253] ACPI: Dynamic OEM Table Load:
[    0.132258] ACPI: SSDT 0xFFFF8A21DED0B000 0005AA (v02 PmRef  ApIst    00003000 INTL 20120913)
[    0.132837] ACPI: Dynamic OEM Table Load:
[    0.132841] ACPI: SSDT 0xFFFF8A21DEDB9A00 000119 (v02 PmRef  ApHwp    00003000 INTL 20120913)
[    0.133212] ACPI: Dynamic OEM Table Load:
[    0.133216] ACPI: SSDT 0xFFFF8A21DEDB8A00 000119 (v02 PmRef  ApCst    00003000 INTL 20120913)
[    0.135590] ACPI: Interpreter enabled
[    0.135632] ACPI: (supports S0 S3 S4 S5)
[    0.135633] ACPI: Using IOAPIC for interrupt routing
[    0.135670] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.136398] ACPI: Enabled 7 GPEs in block 00 to 7F
[    0.139404] ACPI: Power Resource [WRST] (off)
[    0.139564] ACPI: Power Resource [WRST] (off)
[    0.139721] ACPI: Power Resource [WRST] (off)
[    0.139878] ACPI: Power Resource [WRST] (off)
[    0.140040] ACPI: Power Resource [WRST] (off)
[    0.140210] ACPI: Power Resource [WRST] (off)
[    0.140369] ACPI: Power Resource [WRST] (off)
[    0.140524] ACPI: Power Resource [WRST] (off)
[    0.140682] ACPI: Power Resource [WRST] (off)
[    0.140841] ACPI: Power Resource [WRST] (off)
[    0.140998] ACPI: Power Resource [WRST] (off)
[    0.141157] ACPI: Power Resource [WRST] (off)
[    0.141505] ACPI: Power Resource [WRST] (off)
[    0.141684] ACPI: Power Resource [WRST] (off)
[    0.141841] ACPI: Power Resource [WRST] (off)
[    0.142000] ACPI: Power Resource [WRST] (off)
[    0.142156] ACPI: Power Resource [WRST] (off)
[    0.142318] ACPI: Power Resource [WRST] (off)
[    0.142474] ACPI: Power Resource [WRST] (off)
[    0.142631] ACPI: Power Resource [WRST] (off)
[    0.154766] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-fe])
[    0.154772] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.156406] acpi PNP0A08:00: _OSC: OS now controls [PCIeHotplug PME AER PCIeCapability]
[    0.156407] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
[    0.157003] PCI host bridge to bus 0000:00
[    0.157005] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.157007] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.157008] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.157009] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000c3fff window]
[    0.157010] pci_bus 0000:00: root bus resource [mem 0x000c4000-0x000c7fff window]
[    0.157012] pci_bus 0000:00: root bus resource [mem 0x000c8000-0x000cbfff window]
[    0.157013] pci_bus 0000:00: root bus resource [mem 0x000cc000-0x000cffff window]
[    0.157014] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
[    0.157015] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
[    0.157017] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
[    0.157018] pci_bus 0000:00: root bus resource [mem 0x000dc000-0x000dffff window]
[    0.157019] pci_bus 0000:00: root bus resource [mem 0x000e0000-0x000e3fff window]
[    0.157020] pci_bus 0000:00: root bus resource [mem 0x000e4000-0x000e7fff window]
[    0.157022] pci_bus 0000:00: root bus resource [mem 0x000e8000-0x000ebfff window]
[    0.157023] pci_bus 0000:00: root bus resource [mem 0x000ec000-0x000effff window]
[    0.157024] pci_bus 0000:00: root bus resource [mem 0x8d000000-0xdfffffff window]
[    0.157025] pci_bus 0000:00: root bus resource [mem 0xfd000000-0xfe7fffff window]
[    0.157027] pci_bus 0000:00: root bus resource [bus 00-fe]
[    0.157037] pci 0000:00:00.0: [8086:1904] type 00 class 0x060000
[    0.157165] pci 0000:00:02.0: [8086:1916] type 00 class 0x030000
[    0.157177] pci 0000:00:02.0: reg 0x10: [mem 0xde000000-0xdeffffff 64bit]
[    0.157184] pci 0000:00:02.0: reg 0x18: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.157189] pci 0000:00:02.0: reg 0x20: [io  0xf000-0xf03f]
[    0.157324] pci 0000:00:04.0: [8086:1903] type 00 class 0x118000
[    0.157339] pci 0000:00:04.0: reg 0x10: [mem 0xdfb20000-0xdfb27fff 64bit]
[    0.157553] pci 0000:00:14.0: [8086:9d2f] type 00 class 0x0c0330
[    0.157578] pci 0000:00:14.0: reg 0x10: [mem 0xdfb10000-0xdfb1ffff 64bit]
[    0.157658] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.157788] pci 0000:00:14.2: [8086:9d31] type 00 class 0x118000
[    0.157812] pci 0000:00:14.2: reg 0x10: [mem 0xdfb38000-0xdfb38fff 64bit]
[    0.158066] pci 0000:00:15.0: [8086:9d60] type 00 class 0x118000
[    0.158329] pci 0000:00:15.0: reg 0x10: [mem 0xdfb37000-0xdfb37fff 64bit]
[    0.159296] pci 0000:00:15.1: [8086:9d61] type 00 class 0x118000
[    0.159559] pci 0000:00:15.1: reg 0x10: [mem 0xdfb36000-0xdfb36fff 64bit]
[    0.160456] pci 0000:00:16.0: [8086:9d3a] type 00 class 0x078000
[    0.160485] pci 0000:00:16.0: reg 0x10: [mem 0xdfb35000-0xdfb35fff 64bit]
[    0.160569] pci 0000:00:16.0: PME# supported from D3hot
[    0.160708] pci 0000:00:17.0: [8086:9d03] type 00 class 0x010601
[    0.160729] pci 0000:00:17.0: reg 0x10: [mem 0xdfb30000-0xdfb31fff]
[    0.160737] pci 0000:00:17.0: reg 0x14: [mem 0xdfb34000-0xdfb340ff]
[    0.160746] pci 0000:00:17.0: reg 0x18: [io  0xf090-0xf097]
[    0.160754] pci 0000:00:17.0: reg 0x1c: [io  0xf080-0xf083]
[    0.160762] pci 0000:00:17.0: reg 0x20: [io  0xf060-0xf07f]
[    0.160771] pci 0000:00:17.0: reg 0x24: [mem 0xdfb33000-0xdfb337ff]
[    0.160820] pci 0000:00:17.0: PME# supported from D3hot
[    0.160960] pci 0000:00:1c.0: [8086:9d10] type 01 class 0x060400
[    0.161054] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.161235] pci 0000:00:1c.7: [8086:9d17] type 01 class 0x060400
[    0.161328] pci 0000:00:1c.7: PME# supported from D0 D3hot D3cold
[    0.161496] pci 0000:00:1f.0: [8086:9d48] type 00 class 0x060100
[    0.161738] pci 0000:00:1f.2: [8086:9d21] type 00 class 0x058000
[    0.161755] pci 0000:00:1f.2: reg 0x10: [mem 0xdfb2c000-0xdfb2ffff]
[    0.161938] pci 0000:00:1f.3: [8086:9d70] type 00 class 0x040300
[    0.161969] pci 0000:00:1f.3: reg 0x10: [mem 0xdfb28000-0xdfb2bfff 64bit]
[    0.162004] pci 0000:00:1f.3: reg 0x20: [mem 0xdfb00000-0xdfb0ffff 64bit]
[    0.162062] pci 0000:00:1f.3: PME# supported from D3hot D3cold
[    0.162257] pci 0000:00:1f.4: [8086:9d23] type 00 class 0x0c0500
[    0.162319] pci 0000:00:1f.4: reg 0x10: [mem 0xdfb32000-0xdfb320ff 64bit]
[    0.162390] pci 0000:00:1f.4: reg 0x20: [io  0xf040-0xf05f]
[    0.162644] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.162648] pci 0000:00:1c.0:   bridge window [io  0xe000-0xefff]
[    0.162651] pci 0000:00:1c.0:   bridge window [mem 0xdf000000-0xdf9fffff]
[    0.162656] pci 0000:00:1c.0:   bridge window [mem 0xd0000000-0xd09fffff 64bit pref]
[    0.162976] pci 0000:02:00.0: [8086:095a] type 00 class 0x028000
[    0.163082] pci 0000:02:00.0: reg 0x10: [mem 0xdfa00000-0xdfa01fff 64bit]
[    0.163419] pci 0000:02:00.0: PME# supported from D0 D3hot D3cold
[    0.172225] pci 0000:00:1c.7: PCI bridge to [bus 02]
[    0.172230] pci 0000:00:1c.7:   bridge window [mem 0xdfa00000-0xdfafffff]
[    0.174526] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174590] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 *10 11 12 14 15)
[    0.174651] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174713] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174774] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174835] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174896] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174957] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.175555] ACPI: EC: EC stopped
[    0.175556] ACPI: EC: EC started
[    0.175556] ACPI: EC: interrupt blocked
[    0.175757] ACPI: EC: interrupt unblocked
[    0.175777] ACPI: EC: event unblocked
[    0.175790] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0x50, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.175791] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot ECDT EC to handle transactions and events
[    0.175880] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0x50, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.175882] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot DSDT EC to handle transactions and events
[    0.176069] SCSI subsystem initialized
[    0.176096] libata version 3.00 loaded.
[    0.176096] pci 0000:00:02.0: vgaarb: setting as boot VGA device
[    0.176096] pci 0000:00:02.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.176096] pci 0000:00:02.0: vgaarb: bridge control possible
[    0.176096] vgaarb: loaded
[    0.176096] ACPI: bus type USB registered
[    0.176096] usbcore: registered new interface driver usbfs
[    0.176096] usbcore: registered new interface driver hub
[    0.176096] usbcore: registered new device driver usb
[    0.176096] EDAC MC: Ver: 3.0.0
[    0.176275] Registered efivars operations
[    0.180457] PCI: Using ACPI for IRQ routing
[    0.207958] PCI: pci_cache_line_size set to 64 bytes
[    0.208347] e820: reserve RAM buffer [mem 0x00058000-0x0005ffff]
[    0.208348] e820: reserve RAM buffer [mem 0x0009e000-0x0009ffff]
[    0.208349] e820: reserve RAM buffer [mem 0x825b4000-0x83ffffff]
[    0.208350] e820: reserve RAM buffer [mem 0x8519e000-0x87ffffff]
[    0.208352] e820: reserve RAM buffer [mem 0x86515000-0x87ffffff]
[    0.208353] e820: reserve RAM buffer [mem 0x87fff000-0x87ffffff]
[    0.208354] e820: reserve RAM buffer [mem 0x472000000-0x473ffffff]
[    0.208427] NetLabel: Initializing
[    0.208428] NetLabel:  domain hash size = 128
[    0.208429] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.208441] NetLabel:  unlabeled traffic allowed by default
[    0.208454] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.208454] hpet0: 8 comparators, 64-bit 24.000000 MHz counter
[    0.210130] clocksource: Switched to clocksource hpet
[    0.216645] VFS: Disk quotas dquot_6.6.0
[    0.216661] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.216746] AppArmor: AppArmor Filesystem Enabled
[    0.216776] pnp: PnP ACPI init
[    0.217096] system 00:00: [io  0x0680-0x069f] has been reserved
[    0.217098] system 00:00: [io  0xffff] has been reserved
[    0.217099] system 00:00: [io  0xffff] has been reserved
[    0.217101] system 00:00: [io  0xffff] has been reserved
[    0.217102] system 00:00: [io  0x1800-0x18fe] has been reserved
[    0.217104] system 00:00: [io  0x164e-0x164f] has been reserved
[    0.217107] system 00:00: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217206] pnp 00:01: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.217239] system 00:02: [io  0x1854-0x1857] has been reserved
[    0.217242] system 00:02: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.217363] system 00:03: [io  0x0240-0x0259] has been reserved
[    0.217365] system 00:03: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217403] pnp 00:04: Plug and Play ACPI device, IDs ATK3001 PNP030b (active)
[    0.217561] system 00:05: [mem 0xfed10000-0xfed17fff] has been reserved
[    0.217562] system 00:05: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.217564] system 00:05: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.217565] system 00:05: [mem 0xe0000000-0xefffffff] has been reserved
[    0.217567] system 00:05: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.217569] system 00:05: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.217570] system 00:05: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.217572] system 00:05: [mem 0xff000000-0xffffffff] has been reserved
[    0.217573] system 00:05: [mem 0xfee00000-0xfeefffff] could not be reserved
[    0.217575] system 00:05: [mem 0xdffe0000-0xdfffffff] has been reserved
[    0.217577] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217612] system 00:06: [mem 0xfd000000-0xfdabffff] has been reserved
[    0.217614] system 00:06: [mem 0xfdad0000-0xfdadffff] has been reserved
[    0.217615] system 00:06: [mem 0xfdb00000-0xfdffffff] has been reserved
[    0.217617] system 00:06: [mem 0xfe000000-0xfe01ffff] could not be reserved
[    0.217618] system 00:06: [mem 0xfe036000-0xfe03bfff] has been reserved
[    0.217620] system 00:06: [mem 0xfe03d000-0xfe3fffff] has been reserved
[    0.217621] system 00:06: [mem 0xfe410000-0xfe7fffff] has been reserved
[    0.217623] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217937] system 00:07: [io  0xff00-0xfffe] has been reserved
[    0.217939] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.219136] system 00:08: [mem 0xfdaf0000-0xfdafffff] has been reserved
[    0.219138] system 00:08: [mem 0xfdae0000-0xfdaeffff] has been reserved
[    0.219139] system 00:08: [mem 0xfdac0000-0xfdacffff] has been reserved
[    0.219141] system 00:08: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.220091] pnp: PnP ACPI: found 9 devices
[    0.228031] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.228057] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.228065] pci 0000:00:1c.0:   bridge window [io  0xe000-0xefff]
[    0.228069] pci 0000:00:1c.0:   bridge window [mem 0xdf000000-0xdf9fffff]
[    0.228072] pci 0000:00:1c.0:   bridge window [mem 0xd0000000-0xd09fffff 64bit pref]
[    0.228077] pci 0000:00:1c.7: PCI bridge to [bus 02]
[    0.228083] pci 0000:00:1c.7:   bridge window [mem 0xdfa00000-0xdfafffff]
[    0.228091] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.228092] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.228094] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.228095] pci_bus 0000:00: resource 7 [mem 0x000c0000-0x000c3fff window]
[    0.228096] pci_bus 0000:00: resource 8 [mem 0x000c4000-0x000c7fff window]
[    0.228097] pci_bus 0000:00: resource 9 [mem 0x000c8000-0x000cbfff window]
[    0.228099] pci_bus 0000:00: resource 10 [mem 0x000cc000-0x000cffff window]
[    0.228100] pci_bus 0000:00: resource 11 [mem 0x000d0000-0x000d3fff window]
[    0.228101] pci_bus 0000:00: resource 12 [mem 0x000d4000-0x000d7fff window]
[    0.228103] pci_bus 0000:00: resource 13 [mem 0x000d8000-0x000dbfff window]
[    0.228104] pci_bus 0000:00: resource 14 [mem 0x000dc000-0x000dffff window]
[    0.228105] pci_bus 0000:00: resource 15 [mem 0x000e0000-0x000e3fff window]
[    0.228107] pci_bus 0000:00: resource 16 [mem 0x000e4000-0x000e7fff window]
[    0.228108] pci_bus 0000:00: resource 17 [mem 0x000e8000-0x000ebfff window]
[    0.228109] pci_bus 0000:00: resource 18 [mem 0x000ec000-0x000effff window]
[    0.228110] pci_bus 0000:00: resource 19 [mem 0x8d000000-0xdfffffff window]
[    0.228112] pci_bus 0000:00: resource 20 [mem 0xfd000000-0xfe7fffff window]
[    0.228113] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.228115] pci_bus 0000:01: resource 1 [mem 0xdf000000-0xdf9fffff]
[    0.228116] pci_bus 0000:01: resource 2 [mem 0xd0000000-0xd09fffff 64bit pref]
[    0.228117] pci_bus 0000:02: resource 1 [mem 0xdfa00000-0xdfafffff]
[    0.228253] NET: Registered protocol family 2
[    0.228401] TCP established hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.228576] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.228688] TCP: Hash tables configured (established 131072 bind 65536)
[    0.228718] UDP hash table entries: 8192 (order: 6, 262144 bytes)
[    0.228756] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes)
[    0.228812] NET: Registered protocol family 1
[    0.228826] pci 0000:00:02.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.229517] PCI: CLS 0 bytes, default 64
[    0.229546] Unpacking initramfs...
[    0.947134] Freeing initrd memory: 48212K
[    0.947200] DMAR: ACPI device "device:6a" under DMAR at fed91000 as 00:15.0
[    0.947203] DMAR: ACPI device "device:6b" under DMAR at fed91000 as 00:15.1
[    0.947217] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.947220] software IO TLB [mem 0x7d57f000-0x8157f000] (64MB) mapped at [ffff8a1dfd57f000-ffff8a1e0157efff]
[    0.947414] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x255cb6cc5db, max_idle_ns: 440795203504 ns
[    0.947537] Scanning for low memory corruption every 60 seconds
[    0.947882] audit: initializing netlink subsys (disabled)
[    0.947963] audit: type=2000 audit(1519512093.947:1): state=initialized audit_enabled=0 res=1
[    0.948323] Initialise system trusted keyrings
[    0.948330] Key type blacklist registered
[    0.948396] workingset: timestamp_bits=36 max_order=22 bucket_order=0
[    0.949346] zbud: loaded
[    0.949840] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.950005] fuse init (API version 7.26)
[    0.952652] Key type asymmetric registered
[    0.952653] Asymmetric key parser 'x509' registered
[    0.952681] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.952743] io scheduler noop registered
[    0.952744] io scheduler deadline registered
[    0.952766] io scheduler cfq registered (default)
[    0.953433] pcieport 0000:00:1c.0: AER enabled with IRQ 122
[    0.953456] pcieport 0000:00:1c.7: AER enabled with IRQ 123
[    0.953472] pcieport 0000:00:1c.0: Signaling PME with IRQ 122
[    0.953483] pcieport 0000:00:1c.7: Signaling PME with IRQ 123
[    0.953504] pciehp 0000:00:1c.0:pcie004: Slot #4 AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug+ Surprise+ Interlock- NoCompl+ LLActRep+
[    0.953579] efifb: probing for efifb
[    0.953589] efifb: framebuffer at 0xc0000000, using 1920k, total 1920k
[    0.953590] efifb: mode is 800x600x32, linelength=3200, pages=1
[    0.953590] efifb: scrolling: redraw
[    0.953592] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    0.953684] Console: switching to colour frame buffer device 100x37
[    0.953694] fb0: EFI VGA frame buffer device
[    0.953698] intel_idle: MWAIT substates: 0x11142120
[    0.953699] intel_idle: v0.4.1 model 0x4E
[    0.953918] intel_idle: lapic_timer_reliable_states 0xffffffff
[    0.954057] ACPI: AC Adapter [AC0] (off-line)
[    0.955332] input: Lid Switch as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0D:00/input/input0
[    0.956570] ACPI: Lid Switch [LID]
[    0.956597] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:00/input/input1
[    0.956659] ACPI: Sleep Button [SLPB]
[    0.956688] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input2
[    0.956740] ACPI: Power Button [PWRF]
[    0.958045] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    0.958161] thermal LNXTHERM:00: registered as thermal_zone0
[    0.958162] ACPI: Thermal Zone [THRM] (31 C)
[    0.958195] GHES: HEST is not enabled!
[    0.958295] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.962967] Linux agpgart interface v0.103
[    0.967570] ACPI: Battery Slot [BAT0] (battery present)
[    0.969430] loop: module loaded
[    0.969553] libphy: Fixed MDIO Bus: probed
[    0.969554] tun: Universal TUN/TAP device driver, 1.6
[    0.969608] PPP generic driver version 2.4.2
[    0.969667] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.969669] ehci-pci: EHCI PCI platform driver
[    0.969677] ehci-platform: EHCI generic platform driver
[    0.969684] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.969685] ohci-pci: OHCI PCI platform driver
[    0.969691] ohci-platform: OHCI generic platform driver
[    0.969696] uhci_hcd: USB Universal Host Controller Interface driver
[    0.969853] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.969857] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
[    0.970962] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x00109810
[    0.970967] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[    0.971051] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.971052] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.971054] usb usb1: Product: xHCI Host Controller
[    0.971055] usb usb1: Manufacturer: Linux 4.13.0-36-generic xhci-hcd
[    0.971056] usb usb1: SerialNumber: 0000:00:14.0
[    0.971167] hub 1-0:1.0: USB hub found
[    0.971187] hub 1-0:1.0: 12 ports detected
[    0.971790] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.971793] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[    0.971829] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003
[    0.971830] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.971831] usb usb2: Product: xHCI Host Controller
[    0.971833] usb usb2: Manufacturer: Linux 4.13.0-36-generic xhci-hcd
[    0.971834] usb usb2: SerialNumber: 0000:00:14.0
[    0.971934] hub 2-0:1.0: USB hub found
[    0.971949] hub 2-0:1.0: 6 ports detected
[    0.972843] i8042: PNP: PS/2 Controller [PNP030b:PS2K] at 0x60,0x64 irq 1
[    0.972844] i8042: PNP: PS/2 appears to have AUX port disabled, if this is incorrect please boot with i8042.nopnp
[    0.974895] serio: i8042 KBD port at 0x60,0x64 irq 1
[    0.975030] mousedev: PS/2 mouse device common for all mice
[    0.975265] rtc_cmos 00:01: RTC can wake from S4
[    0.975664] rtc_cmos 00:01: rtc core: registered rtc_cmos as rtc0
[    0.975749] rtc_cmos 00:01: alarms up to one month, y3k, 242 bytes nvram, hpet irqs
[    0.975754] i2c /dev entries driver
[    0.975790] device-mapper: uevent: version 1.0.3
[    0.975862] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    0.975865] intel_pstate: Intel P-state driver initializing
[    0.976566] intel_pstate: HWP enabled
[    0.976749] ledtrig-cpu: registered to indicate activity on CPUs
[    0.976751] EFI Variables Facility v0.08 2004-May-17
[    0.982128] NET: Registered protocol family 10
[    0.986848] Segment Routing with IPv6
[    0.986867] NET: Registered protocol family 17
[    0.986873] Key type dns_resolver registered
[    0.987613] RAS: Correctable Errors collector initialized.
[    0.987692] microcode: sig=0x406e3, pf=0x80, revision=0x84
[    0.987795] microcode: Microcode Update Driver: v2.2.
[    0.987896] sched_clock: Marking stable (987792532, 0)->(1095725485, -107932953)
[    0.988212] registered taskstats version 1
[    0.988218] Loading compiled-in X.509 certificates
[    0.990149] Loaded X.509 cert 'Build time autogenerated kernel key: 6392960b5d1a7feefef54e83c93c27dba99187fc'
[    0.992105] Loaded UEFI:db cert 'ASUSTeK Notebook SW Key Certificate: b8e581e4df77a5bb4282d5ccfc00c071' linked to secondary sys keyring
[    0.992272] Loaded UEFI:db cert 'ASUSTeK MotherBoard SW Key Certificate: da83b990422ebc8c441f8d8b039a65a2' linked to secondary sys keyring
[    0.992291] Loaded UEFI:db cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4' linked to secondary sys keyring
[    0.992306] Loaded UEFI:db cert 'Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53' linked to secondary sys keyring
[    0.992472] Loaded UEFI:db cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63' linked to secondary sys keyring
[    0.992774] Loaded UEFI:MokListRT cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63' linked to secondary sys keyring
[    0.993084] zswap: loaded using pool lzo/zbud
[    0.997601] Key type big_key registered
[    0.997603] Key type trusted registered
[    0.999635] Key type encrypted registered
[    0.999638] AppArmor: AppArmor sha1 policy hashing enabled
[    0.999644] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    0.999656] evm: HMAC attrs: 0x1
[    1.000740]   Magic number: 6:247:705
[    1.001023] rtc_cmos 00:01: setting system clock to 2018-02-24 22:41:34 UTC (1519512094)
[    1.001088] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    1.001088] EDD information not available.
[    1.001118] PM: Hibernation image not present or could not be loaded.
[    1.002673] Freeing unused kernel memory: 2364K
[    1.002673] Write protecting the kernel read-only data: 18432k
[    1.003154] Freeing unused kernel memory: 2024K
[    1.003374] Freeing unused kernel memory: 88K
[    1.004797] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.004798] x86/mm: Checking user space page tables
[    1.006028] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.014598] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input3
[    1.116777] hidraw: raw HID events driver (C) Jiri Kosina
[    1.117892] ahci 0000:00:17.0: version 3.0
[    1.118195] ahci 0000:00:17.0: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x5 impl SATA mode
[    1.118197] ahci 0000:00:17.0: flags: 64bit ncq pm led clo only pio slum part deso sadm sds apst 
[    1.118574] scsi host0: ahci
[    1.119043] scsi host1: ahci
[    1.119163] scsi host2: ahci
[    1.119218] ata1: SATA max UDMA/133 abar m2048@0xdfb33000 port 0xdfb33100 irq 125
[    1.119218] ata2: DUMMY
[    1.119221] ata3: SATA max UDMA/133 abar m2048@0xdfb33000 port 0xdfb33200 irq 125
[    1.146610] [drm] Memory usable by graphics device = 4096M
[    1.146612] checking generic (c0000000 1e0000) vs hw (c0000000 10000000)
[    1.146613] fb: switching to inteldrmfb from EFI VGA
[    1.146630] Console: switching to colour dummy device 80x25
[    1.146716] [drm] Replacing VGA console driver
[    1.152183] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.152184] [drm] Driver supports precise vblank timestamp query.
[    1.160822] [drm] Finished loading DMC firmware i915/skl_dmc_ver1_26.bin (v1.26)
[    1.161963] i915 0000:00:02.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=io+mem
[    1.170228] [drm] Initialized i915 1.6.0 20170619 for 0000:00:02.0 on minor 0
[    1.172252] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[    1.174621] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input4
[    1.296123] usb 1-6: new high-speed USB device number 2 using xhci_hcd
[    1.433169] ata3: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.433344] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.434681] ata3.00: ATA-9: SanDisk SD8SNAT256G1002, Z2317002, max UDMA/133
[    1.434682] ata3.00: 500118192 sectors, multi 1: LBA48 NCQ (depth 31/32), AA
[    1.435008] ata1.00: supports DRM functions and may not be fully accessible
[    1.435854] ata1.00: disabling queued TRIM support
[    1.435855] ata1.00: ATA-9: Samsung SSD 850 EVO 500GB, EMT02B6Q, max UDMA/133
[    1.435856] ata1.00: 976773168 sectors, multi 1: LBA48 NCQ (depth 31/32), AA
[    1.438151] ata1.00: supports DRM functions and may not be fully accessible
[    1.438947] ata1.00: disabling queued TRIM support
[    1.440744] ata1.00: configured for UDMA/133
[    1.441481] scsi 0:0:0:0: Direct-Access     ATA      Samsung SSD 850  2B6Q PQ: 0 ANSI: 5
[    1.442510] ata3.00: configured for UDMA/133
[    1.487145] usb 1-6: New USB device found, idVendor=04f2, idProduct=b57a
[    1.487147] usb 1-6: New USB device strings: Mfr=3, Product=1, SerialNumber=2
[    1.487149] usb 1-6: Product: USB2.0 HD UVC WebCam
[    1.487150] usb 1-6: Manufacturer: Chicony Electronics Co.,Ltd.
[    1.487151] usb 1-6: SerialNumber: 0x0001
[    1.496341] sd 0:0:0:0: [sda] 976773168 512-byte logical blocks: (500 GB/466 GiB)
[    1.496355] sd 0:0:0:0: [sda] Write Protect is off
[    1.496357] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    1.496371] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    1.496373] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.496660] scsi 2:0:0:0: Direct-Access     ATA      SanDisk SD8SNAT2 7002 PQ: 0 ANSI: 5
[    1.498623]  sda: sda1 sda2
[    1.499709] sd 0:0:0:0: [sda] supports TCG Opal
[    1.499710] sd 0:0:0:0: [sda] Attached SCSI disk
[    1.544372] sd 2:0:0:0: Attached scsi generic sg1 type 0
[    1.544814] sd 2:0:0:0: [sdb] 500118192 512-byte logical blocks: (256 GB/238 GiB)
[    1.544886] sd 2:0:0:0: [sdb] Write Protect is off
[    1.544888] sd 2:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[    1.544989] sd 2:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.549696]  sdb: sdb1 sdb2 sdb3
[    1.551368] sd 2:0:0:0: [sdb] Attached SCSI disk
[    1.562322] fbcon: inteldrmfb (fb0) is primary device
[    1.562391] Console: switching to colour frame buffer device 240x67
[    1.562415] i915 0000:00:02.0: fb0: inteldrmfb frame buffer device
[    1.668037] usb 1-8: new full-speed USB device number 3 using xhci_hcd
[    1.679523] EXT4-fs (sdb2): mounted filesystem with ordered data mode. Opts: (null)
[    1.810500] usb 1-8: New USB device found, idVendor=8087, idProduct=0a2a
[    1.810502] usb 1-8: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.887542] systemd[1]: systemd 229 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN)
[    1.887675] systemd[1]: Detected architecture x86-64.
[    1.887974] systemd[1]: Set hostname to <wispDev>.
[    1.952342] clocksource: Switched to clocksource tsc
[    2.013750] systemd[1]: Created slice System Slice.
[    2.013922] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[    2.013956] systemd[1]: Listening on Journal Socket (/dev/log).
[    2.013965] systemd[1]: Reached target User and Group Name Lookups.
[    2.013995] systemd[1]: Started Trigger resolvconf update for networkd DNS.
[    2.014013] systemd[1]: Listening on Syslog Socket.
[    2.014060] systemd[1]: Listening on Journal Audit Socket.
[    2.077496] lp: driver loaded but no devices found
[    2.089413] ppdev: user-space parallel port driver
[    2.196712] EXT4-fs (sdb2): re-mounted. Opts: errors=remount-ro
[    2.210299] systemd-journald[252]: Received request to flush runtime journal from PID 1
[    2.270849] input: Asus Wireless Radio Control as /devices/LNXSYSTM:00/LNXSYBUS:00/ATK4002:00/input/input5
[    2.291634] tpm_crb MSFT0101:00: [Firmware Bug]: ACPI region does not cover the entire command/response buffer. [mem 0xfed40000-0xfed4087f flags 0x200] vs fed40080 f80
[    2.291643] tpm_crb MSFT0101:00: [Firmware Bug]: ACPI region does not cover the entire command/response buffer. [mem 0xfed40000-0xfed4087f flags 0x200] vs fed40080 f80
[    2.300041] Bluetooth: Core ver 2.22
[    2.300054] NET: Registered protocol family 31
[    2.300055] Bluetooth: HCI device and connection manager initialized
[    2.300058] Bluetooth: HCI socket layer initialized
[    2.300060] Bluetooth: L2CAP socket layer initialized
[    2.300064] Bluetooth: SCO socket layer initialized
[    2.323758] Bluetooth: HCI UART driver ver 2.3
[    2.323760] Bluetooth: HCI UART protocol H4 registered
[    2.323760] Bluetooth: HCI UART protocol BCSP registered
[    2.323774] Bluetooth: HCI UART protocol LL registered
[    2.323775] Bluetooth: HCI UART protocol ATH3K registered
[    2.323776] Bluetooth: HCI UART protocol Three-wire (H5) registered
[    2.323799] Bluetooth: HCI UART protocol Intel registered
[    2.323812] Bluetooth: HCI UART protocol Broadcom registered
[    2.323813] Bluetooth: HCI UART protocol QCA registered
[    2.323813] Bluetooth: HCI UART protocol AG6XX registered
[    2.323814] Bluetooth: HCI UART protocol Marvell registered
[    2.356775] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    2.360888] mei_me 0000:00:16.0: enabling device (0000 -> 0002)
[    2.365959] intel-lpss 0000:00:15.0: enabling device (0000 -> 0002)
[    2.373558] usbcore: registered new interface driver btusb
[    2.380693] idma64 idma64.0: Found Intel integrated DMA 64-bit
[    2.385874] intel-lpss 0000:00:15.1: enabling device (0000 -> 0002)
[    2.386135] idma64 idma64.1: Found Intel integrated DMA 64-bit
[    2.386955] asus_wmi: ASUS WMI generic driver loaded
[    2.389042] Bluetooth: hci0: read Intel version: 370810011003110e00
[    2.391652] i2c_hid i2c-ELAN1200:00: i2c-ELAN1200:00 supply vdd not found, using dummy regulator
[    2.391681] asus_wmi: Initialization: 0x1
[    2.391721] asus_wmi: BIOS WMI version: 7.9
[    2.391782] asus_wmi: SFUN value: 0xa2065
[    2.393355] input: Asus WMI hotkeys as /devices/platform/asus-nb-wmi/input/input6
[    2.395787] asus_wmi: Number of fans: 1
[    2.413522] Bluetooth: hci0: Intel Bluetooth firmware file: intel/ibt-hw-37.8.10-fw-1.10.3.11.e.bseq
[    2.417101] RAPL PMU: API unit is 2^-32 Joules, 5 fixed counters, 655360 ms ovfl timer
[    2.417102] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[    2.417103] RAPL PMU: hw unit of domain package 2^-14 Joules
[    2.417104] RAPL PMU: hw unit of domain dram 2^-14 Joules
[    2.417105] RAPL PMU: hw unit of domain pp1-gpu 2^-14 Joules
[    2.417105] RAPL PMU: hw unit of domain psys 2^-14 Joules
[    2.420223] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    2.427557] media: Linux media interface: v0.10
[    2.446086] AVX2 version of gcm_enc/dec engaged.
[    2.446087] AES CTR mode by8 optimization enabled
[    2.448099] Linux video capture interface: v2.00
[    2.471933] uvcvideo: Found UVC 1.00 device USB2.0 HD UVC WebCam (04f2:b57a)
[    2.476151] uvcvideo 1-6:1.0: Entity type for entity Realtek Extended Controls Unit was not initialized!
[    2.476154] uvcvideo 1-6:1.0: Entity type for entity Extension 4 was not initialized!
[    2.476155] uvcvideo 1-6:1.0: Entity type for entity Processing 2 was not initialized!
[    2.476157] uvcvideo 1-6:1.0: Entity type for entity Camera 1 was not initialized!
[    2.476221] input: USB2.0 HD UVC WebCam: USB2.0 HD as /devices/pci0000:00/0000:00:14.0/usb1/1-6/1-6:1.0/input/input7
[    2.476276] usbcore: registered new interface driver uvcvideo
[    2.476276] USB Video Class driver (1.1.1)
[    2.481679] Intel(R) Wireless WiFi driver for Linux
[    2.481680] Copyright(c) 2003- 2015 Intel Corporation
[    2.489962] iwlwifi 0000:02:00.0: loaded firmware version 29.610311.0 op_mode iwlmvm
[    2.518559] iwlwifi 0000:02:00.0: Detected Intel(R) Dual Band Wireless AC 7265, REV=0x210
[    2.538935] iwlwifi 0000:02:00.0: base HW address: a4:02:b9:82:12:43
[    2.573464] intel_rapl: Found RAPL domain package
[    2.573465] intel_rapl: Found RAPL domain core
[    2.573466] intel_rapl: Found RAPL domain uncore
[    2.573467] intel_rapl: Found RAPL domain dram
[    2.612647] ieee80211 phy0: Selected rate control algorithm 'iwl-mvm-rs'
[    2.612885] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    2.612901] thermal thermal_zone9: failed to read out thermal zone (-5)
[    2.654857] hid-multitouch 0018:04F3:3022.0001: Ignoring the extra HID_DG_INPUTMODE
[    2.654921] input: ELAN1200:00 04F3:3022 Touchpad as /devices/pci0000:00/0000:00:15.1/i2c_designware.1/i2c-6/i2c-ELAN1200:00/0018:04F3:3022.0001/input/input9
[    2.655885] hid-multitouch 0018:04F3:3022.0001: input,hidraw0: I2C HID v1.00 Mouse [ELAN1200:00 04F3:3022] on i2c-ELAN1200:00
[    2.673380] iwlwifi 0000:02:00.0 wlp2s0: renamed from wlan0
[    2.681327] Adding 16637948k swap on /dev/sdb3.  Priority:-1 extents:1 across:16637948k SSFS
[    2.709114] Bluetooth: hci0: Intel Bluetooth firmware patch completed and activated
[    2.816261] [drm] RC6 on
[    3.714623] snd_hda_intel 0000:00:1f.3: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
[    3.740241] snd_hda_codec_generic hdaudioC0D0: autoconfig for Generic: line_outs=1 (0x17/0x0/0x0/0x0/0x0) type:speaker
[    3.740243] snd_hda_codec_generic hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[    3.740244] snd_hda_codec_generic hdaudioC0D0:    hp_outs=1 (0x16/0x0/0x0/0x0/0x0)
[    3.740245] snd_hda_codec_generic hdaudioC0D0:    mono: mono_out=0x0
[    3.740246] snd_hda_codec_generic hdaudioC0D0:    inputs:
[    3.740247] snd_hda_codec_generic hdaudioC0D0:      Internal Mic=0x1a
[    3.740248] snd_hda_codec_generic hdaudioC0D0:      Mic=0x19
[    3.750660] input: HDA Intel PCH Mic as /devices/pci0000:00/0000:00:1f.3/sound/card0/input10
[    3.750715] input: HDA Intel PCH Headphone as /devices/pci0000:00/0000:00:1f.3/sound/card0/input11
[    3.750768] input: HDA Intel PCH HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input12
[    3.750839] input: HDA Intel PCH HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input13
[    3.750904] input: HDA Intel PCH HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input14
[    3.750956] input: HDA Intel PCH HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input15
[    3.751002] input: HDA Intel PCH HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input16
[    3.772800] random: crng init done
[    4.187839] audit: type=1400 audit(1519512097.686:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=755 comm="apparmor_parser"
[    4.187843] audit: type=1400 audit(1519512097.686:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=755 comm="apparmor_parser"
[    4.187845] audit: type=1400 audit(1519512097.686:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=755 comm="apparmor_parser"
[    4.187847] audit: type=1400 audit(1519512097.686:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=755 comm="apparmor_parser"
[    4.192487] audit: type=1400 audit(1519512097.691:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session" pid=754 comm="apparmor_parser"
[    4.192490] audit: type=1400 audit(1519512097.691:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session//chromium" pid=754 comm="apparmor_parser"
[    4.201947] audit: type=1400 audit(1519512097.701:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="webbrowser-app" pid=758 comm="apparmor_parser"
[    4.201950] audit: type=1400 audit(1519512097.701:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="webbrowser-app//oxide_helper" pid=758 comm="apparmor_parser"
[    4.203340] audit: type=1400 audit(1519512097.702:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=759 comm="apparmor_parser"
[    4.324714] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[    4.324715] Bluetooth: BNEP filters: protocol multicast
[    4.324718] Bluetooth: BNEP socket layer initialized
[    4.783079] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[    4.925675] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[    5.023672] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[    5.070636] Guest personality initialized and is inactive
[    5.070673] VMCI host device registered (name=vmci, major=10, minor=54)
[    5.070674] Initialized host personality
[    5.117660] NET: Registered protocol family 40
[    5.948057] NET: Unregistered protocol family 40
[    6.634252] Bluetooth: RFCOMM TTY layer initialized
[    6.634256] Bluetooth: RFCOMM socket layer initialized
[    6.634260] Bluetooth: RFCOMM ver 1.11
[   11.904772] wlp2s0: authenticate with 88:ad:43:b9:2d:a8
[   11.910624] wlp2s0: send auth to 88:ad:43:b9:2d:a8 (try 1/3)
[   11.913341] wlp2s0: authenticated
[   11.916024] wlp2s0: associate with 88:ad:43:b9:2d:a8 (try 1/3)
[   11.928836] wlp2s0: RX AssocResp from 88:ad:43:b9:2d:a8 (capab=0x411 status=0 aid=1)
[   11.930532] wlp2s0: associated
[   11.930572] IPv6: ADDRCONF(NETDEV_CHANGE): wlp2s0: link becomes ready
[   12.001717] wlp2s0: Limiting TX power to 14 (17 - 3) dBm as advertised by 88:ad:43:b9:2d:a8
[   13.928512] vmmon: loading out-of-tree module taints kernel.
[   13.928562] vmmon: module verification failed: signature and/or required key missing - tainting kernel
[   13.929343] /dev/vmmon[3143]: Module vmmon: registered with major=10 minor=165
[   13.929345] /dev/vmmon[3143]: Using tsc_khz as TSC frequency: 2592000
[   13.929346] /dev/vmmon[3143]: Module vmmon: initialized
[   13.942494] Guest personality initialized and is inactive
[   13.942791] VMCI host device registered (name=vmci, major=10, minor=54)
[   13.942792] Initialized host personality
[   13.960443] NET: Registered protocol family 40
[   14.047694] /dev/vmnet: open called by PID 3260 (vmnet-bridge)
[   14.047698] /dev/vmnet: hub 0 does not exist, allocating memory.
[   14.047717] /dev/vmnet: port on hub 0 successfully opened
[   14.047724] bridge-wlp2s0: device is wireless, enabling SMAC
[   14.047726] bridge-wlp2s0: up
[   14.047729] bridge-wlp2s0: attached
[   15.064107] /dev/vmnet: open called by PID 3430 (vmnet-netifup)
[   15.064111] /dev/vmnet: hub 1 does not exist, allocating memory.
[   15.064124] /dev/vmnet: port on hub 1 successfully opened
[   15.090087] /dev/vmnet: open called by PID 3432 (vmnet-dhcpd)
[   15.090095] /dev/vmnet: port on hub 1 successfully opened
[   15.110927] /dev/vmnet: open called by PID 3457 (vmnet-natd)
[   15.110932] /dev/vmnet: hub 8 does not exist, allocating memory.
[   15.110952] /dev/vmnet: port on hub 8 successfully opened
[   15.112098] userif-3: sent link down event.
[   15.112100] userif-3: sent link up event.
[   15.114083] /dev/vmnet: open called by PID 3459 (vmnet-netifup)
[   15.114092] /dev/vmnet: port on hub 8 successfully opened
[   15.132276] /dev/vmnet: open called by PID 3466 (vmnet-dhcpd)
[   15.132284] /dev/vmnet: port on hub 8 successfully opened
[  103.537421] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[  103.537433] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[  103.537437] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[  103.537439] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[  147.057666] asus_wmi: Unknown key cf pressed
[  523.790092] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[  523.790122] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[  523.790144] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[  523.790159] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 1254.016417] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 1254.016445] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 1254.016474] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 1254.016478] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 1617.645195] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 1617.645220] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 1617.645237] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 1617.645248] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 2344.904744] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 2344.904812] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 2344.904833] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 2344.904845] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 2429.795677] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 2429.795701] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 2429.795718] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 2429.795730] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4002.397679] iwlwifi 0000:02:00.0: Microcode SW error detected.  Restarting 0x2000000.
[ 4002.397812] iwlwifi 0000:02:00.0: Start IWL Error Log Dump:
[ 4002.397815] iwlwifi 0000:02:00.0: Status: 0x00000200, count: 6
[ 4002.397818] iwlwifi 0000:02:00.0: Loaded firmware version: 29.610311.0
[ 4002.397820] iwlwifi 0000:02:00.0: 0x0000105C | ADVANCED_SYSASSERT          
[ 4002.397822] iwlwifi 0000:02:00.0: 0x00000220 | trm_hw_status0
[ 4002.397825] iwlwifi 0000:02:00.0: 0x00000000 | trm_hw_status1
[ 4002.397827] iwlwifi 0000:02:00.0: 0x00043D58 | branchlink2
[ 4002.397829] iwlwifi 0000:02:00.0: 0x0004B016 | interruptlink1
[ 4002.397831] iwlwifi 0000:02:00.0: 0x00000000 | interruptlink2
[ 4002.397833] iwlwifi 0000:02:00.0: 0xDEADBEEF | data1
[ 4002.397836] iwlwifi 0000:02:00.0: 0xDEADBEEF | data2
[ 4002.397838] iwlwifi 0000:02:00.0: 0xDEADBEEF | data3
[ 4002.397840] iwlwifi 0000:02:00.0: 0x0E017A98 | beacon time
[ 4002.397842] iwlwifi 0000:02:00.0: 0x3186A56B | tsf low
[ 4002.397844] iwlwifi 0000:02:00.0: 0x0000002B | tsf hi
[ 4002.397845] iwlwifi 0000:02:00.0: 0x00000000 | time gp1
[ 4002.397847] iwlwifi 0000:02:00.0: 0xEE458B6C | time gp2
[ 4002.397849] iwlwifi 0000:02:00.0: 0x00000001 | uCode revision type
[ 4002.397851] iwlwifi 0000:02:00.0: 0x0000001D | uCode version major
[ 4002.397853] iwlwifi 0000:02:00.0: 0x00095007 | uCode version minor
[ 4002.397855] iwlwifi 0000:02:00.0: 0x00000210 | hw version
[ 4002.397857] iwlwifi 0000:02:00.0: 0x00489200 | board version
[ 4002.397859] iwlwifi 0000:02:00.0: 0x0A04001C | hcmd
[ 4002.397861] iwlwifi 0000:02:00.0: 0x24022002 | isr0
[ 4002.397863] iwlwifi 0000:02:00.0: 0x00800000 | isr1
[ 4002.397865] iwlwifi 0000:02:00.0: 0x00000002 | isr2
[ 4002.397867] iwlwifi 0000:02:00.0: 0x00417CC1 | isr3
[ 4002.397869] iwlwifi 0000:02:00.0: 0x00000000 | isr4
[ 4002.397871] iwlwifi 0000:02:00.0: 0x0A03001C | last cmd Id
[ 4002.397873] iwlwifi 0000:02:00.0: 0x00000000 | wait_event
[ 4002.397875] iwlwifi 0000:02:00.0: 0x000000D4 | l2p_control
[ 4002.397877] iwlwifi 0000:02:00.0: 0x00018030 | l2p_duration
[ 4002.397879] iwlwifi 0000:02:00.0: 0x00000007 | l2p_mhvalid
[ 4002.397881] iwlwifi 0000:02:00.0: 0x00000081 | l2p_addr_match
[ 4002.397884] iwlwifi 0000:02:00.0: 0x00000005 | lmpm_pmg_sel
[ 4002.397886] iwlwifi 0000:02:00.0: 0x29102230 | timestamp
[ 4002.397888] iwlwifi 0000:02:00.0: 0x00003848 | flow_handler
[ 4002.397891] ieee80211 phy0: Hardware restart was requested
[ 4002.540189] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4002.540194] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4002.540197] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4002.540200] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4002.620245] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4002.620268] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4002.620289] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4002.620304] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4141.745673] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4141.745685] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4141.745689] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4141.745693] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4332.626563] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4332.626587] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4332.626604] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4332.626615] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4984.107737] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4984.107762] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4984.107778] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4984.107790] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 5295.457653] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 5295.457664] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 5295.457668] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 5295.457670] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 5883.291541] wlp2s0: deauthenticating from 88:ad:43:b9:2d:a8 by local choice (Reason: 3=DEAUTH_LEAVING)
[ 5883.307015] wlp2s0: failed to remove key (1, ff:ff:ff:ff:ff:ff) from hardware (-22)
[ 5883.307196] wlp2s0: failed to remove key (2, ff:ff:ff:ff:ff:ff) from hardware (-22)
[ 5883.308073] bridge-wlp2s0: disabling the bridge on dev down
[ 5883.308101] bridge-wlp2s0: down
[ 5883.308107] bridge-wlp2s0: detached
[ 5883.507422] userif-3: sent link down event.
[ 5883.507425] userif-3: sent link up event.
[ 5884.643364] PM: Syncing filesystems ... done.
[ 5884.649669] PM: Preparing system for sleep (mem)
[ 5884.652071] Freezing user space processes ... (elapsed 0.001 seconds) done.
[ 5884.654022] OOM killer disabled.
[ 5884.654022] Freezing remaining freezable tasks ... (elapsed 0.000 seconds) done.
[ 5884.654843] PM: Suspending system (mem)
[ 5884.654880] Suspending console(s) (use no_console_suspend to debug)
[ 5884.871980] sd 2:0:0:0: [sdb] Synchronizing SCSI cache
[ 5884.872111] sd 2:0:0:0: [sdb] Stopping disk
[ 5884.872195] sd 0:0:0:0: [sda] Synchronizing SCSI cache
[ 5884.874473] sd 0:0:0:0: [sda] Stopping disk
[ 5886.157004] PM: suspend of devices complete after 1285.783 msecs
[ 5886.174739] PM: late suspend of devices complete after 17.712 msecs
[ 5886.214758] PM: noirq suspend of devices complete after 40.018 msecs
[ 5886.215106] ACPI: Preparing to enter system sleep state S3
[ 5886.225502] ACPI: EC: event blocked
[ 5886.225503] ACPI: EC: EC stopped
[ 5886.225503] PM: Saving platform NVS memory
[ 5886.225606] Disabling non-boot CPUs ...
[ 5886.247167] IRQ 128: no longer affine to CPU1
[ 5886.248184] smpboot: CPU 1 is now offline
[ 5886.267540] IRQ 123: no longer affine to CPU2
[ 5886.267550] IRQ 124: no longer affine to CPU2
[ 5886.267559] IRQ 125: no longer affine to CPU2
[ 5886.269988] smpboot: CPU 2 is now offline
[ 5886.291443] IRQ 1: no longer affine to CPU3
[ 5886.291454] IRQ 8: no longer affine to CPU3
[ 5886.291463] IRQ 9: no longer affine to CPU3
[ 5886.291474] IRQ 16: no longer affine to CPU3
[ 5886.291485] IRQ 17: no longer affine to CPU3
[ 5886.291496] IRQ 109: no longer affine to CPU3
[ 5886.292573] smpboot: CPU 3 is now offline
[ 5886.297070] ACPI: Low-level resume complete
[ 5886.297190] ACPI: EC: EC started
[ 5886.297191] PM: Restoring platform NVS memory
[ 5886.298020] Suspended for 6102.426 seconds
[ 5886.298095] Enabling non-boot CPUs ...
[ 5886.298139] x86: Booting SMP configuration:
[ 5886.298140] smpboot: Booting Node 0 Processor 1 APIC 0x2
[ 5886.298713]  cache: parent cpu1 should not be sleeping
[ 5886.298885] CPU1 is up
[ 5886.298908] smpboot: Booting Node 0 Processor 2 APIC 0x1
[ 5886.299477]  cache: parent cpu2 should not be sleeping
[ 5886.299660] CPU2 is up
[ 5886.299685] smpboot: Booting Node 0 Processor 3 APIC 0x3
[ 5886.300188]  cache: parent cpu3 should not be sleeping
[ 5886.300422] CPU3 is up
[ 5886.304301] ACPI: Waking up from system sleep state S3
[ 5886.361549] PM: noirq resume of devices complete after 41.627 msecs
[ 5886.373120] PM: early resume of devices complete after 11.524 msecs
[ 5886.373330] ACPI: EC: event unblocked
[ 5886.373446] usb usb1: root hub lost power or was reset
[ 5886.373450] usb usb2: root hub lost power or was reset
[ 5886.373971] sd 0:0:0:0: [sda] Starting disk
[ 5886.373974] sd 2:0:0:0: [sdb] Starting disk
[ 5886.374613] iwlwifi 0000:02:00.0: RF_KILL bit toggled to enable radio.
[ 5886.384282] ACPI: button: The lid device is not compliant to SW_LID.
[ 5886.384481] rtc_cmos 00:01: Alarms can be up to one month in the future
[ 5886.687687] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[ 5886.687899] ata3: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[ 5886.688095] ata1.00: supports DRM functions and may not be fully accessible
[ 5886.689196] ata1.00: disabling queued TRIM support
[ 5886.691604] ata1.00: supports DRM functions and may not be fully accessible
[ 5886.692340] ata1.00: disabling queued TRIM support
[ 5886.694174] ata1.00: configured for UDMA/133
[ 5886.697127] ata3.00: configured for UDMA/133
[ 5886.723694] usb 1-6: reset high-speed USB device number 2 using xhci_hcd
[ 5886.783585] /dev/vmmon[0]: HostIFReadUptimeWork: detected settimeofday: fixed uptimeBase old 18445224561602123209 new 18445224555499697001 attempts 1
[ 5886.983901] usb 1-8: reset full-speed USB device number 3 using xhci_hcd
[ 5887.143066] PM: resume of devices complete after 769.948 msecs
[ 5887.143181] usb 1-8:1.0: rebind failed: -517
[ 5887.143186] usb 1-8:1.1: rebind failed: -517
[ 5887.145449] PM: Finishing wakeup.
[ 5887.145451] OOM killer enabled.
[ 5887.145452] Restarting tasks ... done.
[ 5887.160920] thermal thermal_zone9: failed to read out thermal zone (-5)
[ 5887.175561] Bluetooth: hci0: read Intel version: 370810011003110e00
[ 5887.175564] Bluetooth: hci0: Intel Bluetooth firmware file: intel/ibt-hw-37.8.10-fw-1.10.3.11.e.bseq
[ 5887.209791] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[ 5887.262954] [drm] RC6 on
[ 5887.320035] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[ 5887.376178] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[ 5887.483576] Bluetooth: hci0: Intel Bluetooth firmware patch completed and activated
[ 5891.547772] wlp2s0: authenticate with 88:ad:43:b9:2d:a8
[ 5891.557602] wlp2s0: send auth to 88:ad:43:b9:2d:a8 (try 1/3)
[ 5891.562644] wlp2s0: authenticated
[ 5891.567537] wlp2s0: associate with 88:ad:43:b9:2d:a8 (try 1/3)
[ 5891.581208] wlp2s0: RX AssocResp from 88:ad:43:b9:2d:a8 (capab=0x411 status=0 aid=1)
[ 5891.595382] wlp2s0: associated
[ 5891.595553] wlp2s0: Limiting TX power to 14 (17 - 3) dBm as advertised by 88:ad:43:b9:2d:a8
[ 5891.596346] IPv6: ADDRCONF(NETDEV_CHANGE): wlp2s0: link becomes ready
[ 5891.618368] /dev/vmnet: open called by PID 3260 (vmnet-bridge)
[ 5891.618382] /dev/vmnet: hub 0 does not exist, allocating memory.
[ 5891.618446] /dev/vmnet: port on hub 0 successfully opened
[ 5891.618465] bridge-wlp2s0: device is wireless, enabling SMAC
[ 5891.618469] bridge-wlp2s0: up
[ 5891.618784] bridge-wlp2s0: attached
[ 5891.818224] userif-3: sent link down event.
[ 5891.818225] userif-3: sent link up event.
[ 5895.394011] userif-3: sent link down event.
[ 5895.394019] userif-3: sent link up event.[    0.000000] random: get_random_bytes called from start_kernel+0x42/0x50d with crng_init=0
[    0.000000] Linux version 4.13.0-36-generic (buildd@lgw01-amd64-033) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.9)) #40~16.04.1-Ubuntu SMP Fri Feb 16 23:25:58 UTC 2018 (Ubuntu 4.13.0-36.40~16.04.1-generic 4.13.13)
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-36-generic.efi.signed root=UUID=c6b9b4d6-4292-4129-9a38-b57109cac95d ro quiet splash vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x008: 'MPX bounds registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x010: 'MPX CSR'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: xstate_offset[3]:  832, xstate_sizes[3]:   64
[    0.000000] x86/fpu: xstate_offset[4]:  896, xstate_sizes[4]:   64
[    0.000000] x86/fpu: Enabled xstate features 0x1f, context size is 960 bytes, using 'compacted' format.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000057fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000000058000-0x0000000000058fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000059000-0x000000000009dfff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009e000-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000825b3fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000825b4000-0x00000000825b4fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000825b5000-0x00000000825defff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000825df000-0x000000008519dfff] usable
[    0.000000] BIOS-e820: [mem 0x000000008519e000-0x0000000085e79fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000085e7a000-0x0000000086514fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000086515000-0x00000000870a4fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000870a5000-0x0000000087efffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000087f00000-0x0000000087f7efff] type 20
[    0.000000] BIOS-e820: [mem 0x0000000087f7f000-0x0000000087ffefff] usable
[    0.000000] BIOS-e820: [mem 0x0000000088000000-0x00000000880fffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000e0000000-0x00000000efffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fe000000-0x00000000fe010fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x0000000471ffffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] efi: EFI v2.40 by American Megatrends
[    0.000000] efi:  ESRT=0x87e47e18  ACPI=0x86619000  ACPI 2.0=0x86619000  SMBIOS=0x87661000  SMBIOS 3.0=0x87660000 
[    0.000000] random: fast init done
[    0.000000] SMBIOS 3.0.0 present.
[    0.000000] DMI: ASUSTeK COMPUTER INC. UX310UA/UX310UA, BIOS UX310UA.202 05/18/2016
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x472000 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: write-back
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF uncachable
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 00C0000000 mask 7FC0000000 uncachable
[    0.000000]   1 base 00A0000000 mask 7FE0000000 uncachable
[    0.000000]   2 base 0090000000 mask 7FF0000000 uncachable
[    0.000000]   3 base 008C000000 mask 7FFC000000 uncachable
[    0.000000]   4 base 008A000000 mask 7FFE000000 uncachable
[    0.000000]   5 base 0089000000 mask 7FFF000000 uncachable
[    0.000000]   6 base 0088800000 mask 7FFF800000 uncachable
[    0.000000]   7 disabled
[    0.000000]   8 disabled
[    0.000000]   9 disabled
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WC  UC- WT  
[    0.000000] e820: last_pfn = 0x87fff max_arch_pfn = 0x400000000
[    0.000000] esrt: Reserving ESRT space from 0x0000000087e47e18 to 0x0000000087e47e50.
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [ffff8a1d80098000] 98000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x3e352a000, 0x3e352afff] PGTABLE
[    0.000000] BRK [0x3e352b000, 0x3e352bfff] PGTABLE
[    0.000000] BRK [0x3e352c000, 0x3e352cfff] PGTABLE
[    0.000000] BRK [0x3e352d000, 0x3e352dfff] PGTABLE
[    0.000000] BRK [0x3e352e000, 0x3e352efff] PGTABLE
[    0.000000] BRK [0x3e352f000, 0x3e352ffff] PGTABLE
[    0.000000] BRK [0x3e3530000, 0x3e3530fff] PGTABLE
[    0.000000] BRK [0x3e3531000, 0x3e3531fff] PGTABLE
[    0.000000] BRK [0x3e3532000, 0x3e3532fff] PGTABLE
[    0.000000] BRK [0x3e3533000, 0x3e3533fff] PGTABLE
[    0.000000] BRK [0x3e3534000, 0x3e3534fff] PGTABLE
[    0.000000] Secure boot could not be determined
[    0.000000] RAMDISK: [mem 0x321c6000-0x350dafff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x0000000086619000 000024 (v02 _ASUS_)
[    0.000000] ACPI: XSDT 0x00000000866190A0 0000C4 (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x000000008663EF50 00010C (v05 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: DSDT 0x00000000866191F8 025D56 (v02 _ASUS_ Notebook 01072009 INTL 20120913)
[    0.000000] ACPI: FACS 0x000000008708BF80 000040
[    0.000000] ACPI: APIC 0x000000008663F060 000084 (v03 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x000000008663F0E8 000044 (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: FIDT 0x000000008663F130 00009C (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: MCFG 0x000000008663F1D0 00003C (v01 _ASUS_ Notebook 01072009 MSFT 00000097)
[    0.000000] ACPI: HPET 0x000000008663F210 000038 (v01 _ASUS_ Notebook 01072009 AMI. 0005000B)
[    0.000000] ACPI: SSDT 0x000000008663F248 000315 (v01 SataRe SataTabl 00001000 INTL 20120913)
[    0.000000] ACPI: ECDT 0x000000008663F560 0000C1 (v01 _ASUS_ Notebook 01072009 AMI. 00000005)
[    0.000000] ACPI: LPIT 0x000000008663F628 000094 (v01 INTEL  SKL-ULT  00000000 MSFT 0000005F)
[    0.000000] ACPI: SSDT 0x000000008663F6C0 000248 (v02 INTEL  sensrhub 00000000 INTL 20120913)
[    0.000000] ACPI: DBGP 0x000000008663F908 000034 (v01 INTEL           00000000 MSFT 0000005F)
[    0.000000] ACPI: DBG2 0x000000008663F940 000054 (v00 INTEL           00000000 MSFT 0000005F)
[    0.000000] ACPI: SSDT 0x000000008663F998 003F2E (v02 DptfTa DptfTabl 00001000 INTL 20120913)
[    0.000000] ACPI: SSDT 0x00000000866438C8 005846 (v02 SaSsdt SaSsdt   00003000 INTL 20120913)
[    0.000000] ACPI: UEFI 0x0000000086649110 000042 (v01                 00000000      00000000)
[    0.000000] ACPI: SSDT 0x0000000086649158 000E73 (v02 CpuRef CpuSsdt  00003000 INTL 20120913)
[    0.000000] ACPI: BGRT 0x0000000086649FD0 000038 (v01 _ASUS_ Notebook 01072009 AMI  00010013)
[    0.000000] ACPI: DMAR 0x000000008664A008 0000F0 (v01 INTEL  SKL      00000001 INTL 00000001)
[    0.000000] ACPI: TPM2 0x000000008664A0F8 000034 (v03        Tpm2Tabl 00000001 AMI  00000000)
[    0.000000] ACPI: MSDM 0x0000000085C3BF18 000055 (v03 _ASUS_ Notebook 00000000 ASUS 00000001)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x0000000471ffffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x471fd5000-0x471ffffff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x0000000471ffffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x0000000000057fff]
[    0.000000]   node   0: [mem 0x0000000000059000-0x000000000009dfff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x00000000825b3fff]
[    0.000000]   node   0: [mem 0x00000000825df000-0x000000008519dfff]
[    0.000000]   node   0: [mem 0x0000000085e7a000-0x0000000086514fff]
[    0.000000]   node   0: [mem 0x0000000087f7f000-0x0000000087ffefff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x0000000471ffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x0000000471ffffff]
[    0.000000] On node 0 totalpages: 4159530
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 22 pages reserved
[    0.000000]   DMA zone: 3996 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 8483 pages used for memmap
[    0.000000]   DMA32 zone: 542862 pages, LIFO batch:31
[    0.000000]   Normal zone: 56448 pages used for memmap
[    0.000000]   Normal zone: 3612672 pages, LIFO batch:31
[    0.000000] Reserving Intel graphics memory at 0x0000000089000000-0x000000008cffffff
[    0.000000] ACPI: PM-Timer IO Port: 0x1808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 2, version 32, address 0xfec00000, GSI 0-119
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x8086a701 base: 0xfed00000
[    0.000000] [Firmware Bug]: TSC_DEADLINE disabled due to Errata; please update microcode to version: 0xb2 (or later)
[    0.000000] smpboot: Allowing 4 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x00058000-0x00058fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009e000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x825b4000-0x825b4fff]
[    0.000000] PM: Registered nosave memory: [mem 0x825b5000-0x825defff]
[    0.000000] PM: Registered nosave memory: [mem 0x8519e000-0x85e79fff]
[    0.000000] PM: Registered nosave memory: [mem 0x86515000-0x870a4fff]
[    0.000000] PM: Registered nosave memory: [mem 0x870a5000-0x87efffff]
[    0.000000] PM: Registered nosave memory: [mem 0x87f00000-0x87f7efff]
[    0.000000] PM: Registered nosave memory: [mem 0x87fff000-0x87ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x88000000-0x880fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x88100000-0x88ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x89000000-0x8cffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x8d000000-0xdfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xe0000000-0xefffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf0000000-0xfdffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe000000-0xfe010fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfe011000-0xfebfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec01000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0x8d000000-0xdfffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:4 nr_cpu_ids:4 nr_node_ids:1
[    0.000000] percpu: Embedded 45 pages/cpu @ffff8a21f1c00000 s146520 r8192 d29608 u524288
[    0.000000] pcpu-alloc: s146520 r8192 d29608 u524288 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 0 1 2 3 
[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 4094513
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-36-generic.efi.signed root=UUID=c6b9b4d6-4292-4129-9a38-b57109cac95d ro quiet splash vt.handoff=7
[    0.000000] PID hash table entries: 4096 (order: 3, 32768 bytes)
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 16176176K/16638120K available (12300K kernel code, 2481K rwdata, 4008K rodata, 2364K init, 2368K bss, 461944K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] Kernel/User page tables isolation: enabled
[    0.000000] ftrace: allocating 37831 entries in 148 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=4.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
[    0.000000] NR_IRQS: 524544, nr_irqs: 1024, preallocated irqs: 16
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635855245 ns
[    0.000000] hpet clockevent registered
[    0.004000] tsc: Detected 2600.000 MHz processor
[    0.004000] Calibrating delay loop (skipped), value calculated using timer frequency.. 5184.00 BogoMIPS (lpj=10368000)
[    0.004000] pid_max: default: 32768 minimum: 301
[    0.004000] ACPI: Core revision 20170531
[    0.042558] ACPI: 6 ACPI AML tables successfully acquired and loaded
[    0.043766] Security Framework initialized
[    0.043767] Yama: becoming mindful.
[    0.043783] AppArmor: AppArmor initialized
[    0.045974] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes)
[    0.047031] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.047070] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.047104] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes)
[    0.047278] CPU: Physical Processor ID: 0
[    0.047279] CPU: Processor Core ID: 0
[    0.047284] ENERGY_PERF_BIAS: Set to 'normal', was 'performance'
[    0.047284] ENERGY_PERF_BIAS: View and update with x86_energy_perf_policy(8)
[    0.047286] FEATURE SPEC_CTRL Not Present
[    0.047290] mce: CPU supports 8 MCE banks
[    0.047299] CPU0: Thermal monitoring enabled (TM1)
[    0.047314] process: using mwait in idle threads
[    0.047316] Last level iTLB entries: 4KB 64, 2MB 8, 4MB 8
[    0.047317] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    0.047318] Spectre V2 mitigation: Mitigation: Full generic retpoline
[    0.047319] Spectre V2 mitigation: Speculation control IBPB not-supported IBRS not-supported
[    0.047320] Spectre V2 mitigation: Filling RSB on context switch
[    0.047842] Freeing SMP alternatives memory: 36K
[    0.051156] smpboot: Max logical packages: 2
[    0.051163] DMAR: Host address width 39
[    0.051164] DMAR: DRHD base: 0x000000fed90000 flags: 0x0
[    0.051171] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap 1c0000c40660462 ecap 7e3ff0505e
[    0.051172] DMAR: DRHD base: 0x000000fed91000 flags: 0x1
[    0.051176] DMAR: dmar1: reg_base_addr fed91000 ver 1:0 cap d2008c40660462 ecap f050da
[    0.051177] DMAR: RMRR base: 0x00000085c1b000 end: 0x00000085c3afff
[    0.051179] DMAR: RMRR base: 0x00000088800000 end: 0x0000008cffffff
[    0.051180] DMAR: ANDD device: 1 name: \_SB.PCI0.I2C0
[    0.051180] DMAR: ANDD device: 2 name: \_SB.PCI0.I2C1
[    0.051182] DMAR-IR: IOAPIC id 2 under DRHD base  0xfed91000 IOMMU 1
[    0.051183] DMAR-IR: HPET id 0 under DRHD base 0xfed91000
[    0.051184] DMAR-IR: x2apic is disabled because BIOS sets x2apic opt out bit.
[    0.051184] DMAR-IR: Use 'intremap=no_x2apic_optout' to override the BIOS setting.
[    0.052649] DMAR-IR: Enabled IRQ remapping in xapic mode
[    0.052650] x2apic: IRQ remapping doesn't support X2APIC mode
[    0.056843] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.100000] smpboot: CPU0: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz (family: 0x6, model: 0x4e, stepping: 0x3)
[    0.100000] Performance Events: PEBS fmt3+, Skylake events, 32-deep LBR, full-width counters, Intel PMU driver.
[    0.100000] ... version:                4
[    0.100000] ... bit width:              48
[    0.100000] ... generic registers:      4
[    0.100000] ... value mask:             0000ffffffffffff
[    0.100000] ... max period:             00007fffffffffff
[    0.100000] ... fixed-purpose events:   3
[    0.100000] ... event mask:             000000070000000f
[    0.100000] Hierarchical SRCU implementation.
[    0.100000] smp: Bringing up secondary CPUs ...
[    0.100000] x86: Booting SMP configuration:
[    0.100000] .... node  #0, CPUs:      #1
[    0.100000] NMI watchdog: enabled on all CPUs, permanently consumes one hw-PMU counter.
[    0.100000]  #2 #3
[    0.100000] smp: Brought up 1 node, 4 CPUs
[    0.100000] smpboot: Total of 4 processors activated (20736.00 BogoMIPS)
[    0.100400] devtmpfs: initialized
[    0.100400] x86/mm: Memory block size: 128MB
[    0.104855] evm: security.selinux
[    0.104856] evm: security.SMACK64
[    0.104856] evm: security.SMACK64EXEC
[    0.104856] evm: security.SMACK64TRANSMUTE
[    0.104857] evm: security.SMACK64MMAP
[    0.104858] evm: security.ima
[    0.104858] evm: security.capability
[    0.104871] PM: Registering ACPI NVS region [mem 0x825b4000-0x825b4fff] (4096 bytes)
[    0.104871] PM: Registering ACPI NVS region [mem 0x86515000-0x870a4fff] (12124160 bytes)
[    0.104871] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.104871] futex hash table entries: 1024 (order: 4, 65536 bytes)
[    0.104871] pinctrl core: initialized pinctrl subsystem
[    0.104871] RTC time: 22:41:33, date: 02/24/18
[    0.104871] NET: Registered protocol family 16
[    0.104871] cpuidle: using governor ladder
[    0.104871] cpuidle: using governor menu
[    0.104871] PCCT header not found.
[    0.104871] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    0.104871] ACPI: bus type PCI registered
[    0.104871] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.104871] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0xe0000000-0xefffffff] (base 0xe0000000)
[    0.104871] PCI: MMCONFIG at [mem 0xe0000000-0xefffffff] reserved in E820
[    0.104871] PCI: Using configuration type 1 for base access
[    0.104871] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.104871] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.104871] ACPI: Added _OSI(Module Device)
[    0.104871] ACPI: Added _OSI(Processor Device)
[    0.104871] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.104871] ACPI: Added _OSI(Processor Aggregator Device)
[    0.104871] ACPI: EC: EC started
[    0.104871] ACPI: EC: interrupt blocked
[    0.109189] ACPI: \: Used as first EC
[    0.109191] ACPI: \: GPE=0x50, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.109192] ACPI: \: Used as boot ECDT EC to handle transactions
[    0.109978] ACPI: Executed 21 blocks of module-level executable AML code
[    0.122346] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.128728] ACPI: Dynamic OEM Table Load:
[    0.128748] ACPI: SSDT 0xFFFF8A21DED0D800 000660 (v02 PmRef  Cpu0Ist  00003000 INTL 20120913)
[    0.129129] ACPI: \_PR_.CPU0: _OSC native thermal LVT Acked
[    0.130616] ACPI: Dynamic OEM Table Load:
[    0.130621] ACPI: SSDT 0xFFFF8A21DED87000 00037F (v02 PmRef  Cpu0Cst  00003001 INTL 20120913)
[    0.130993] ACPI: Dynamic OEM Table Load:
[    0.130997] ACPI: SSDT 0xFFFF8A21DED26480 00008E (v02 PmRef  Cpu0Hwp  00003000 INTL 20120913)
[    0.131270] ACPI: Dynamic OEM Table Load:
[    0.131274] ACPI: SSDT 0xFFFF8A21DEDB8C00 000130 (v02 PmRef  HwpLvt   00003000 INTL 20120913)
[    0.132253] ACPI: Dynamic OEM Table Load:
[    0.132258] ACPI: SSDT 0xFFFF8A21DED0B000 0005AA (v02 PmRef  ApIst    00003000 INTL 20120913)
[    0.132837] ACPI: Dynamic OEM Table Load:
[    0.132841] ACPI: SSDT 0xFFFF8A21DEDB9A00 000119 (v02 PmRef  ApHwp    00003000 INTL 20120913)
[    0.133212] ACPI: Dynamic OEM Table Load:
[    0.133216] ACPI: SSDT 0xFFFF8A21DEDB8A00 000119 (v02 PmRef  ApCst    00003000 INTL 20120913)
[    0.135590] ACPI: Interpreter enabled
[    0.135632] ACPI: (supports S0 S3 S4 S5)
[    0.135633] ACPI: Using IOAPIC for interrupt routing
[    0.135670] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.136398] ACPI: Enabled 7 GPEs in block 00 to 7F
[    0.139404] ACPI: Power Resource [WRST] (off)
[    0.139564] ACPI: Power Resource [WRST] (off)
[    0.139721] ACPI: Power Resource [WRST] (off)
[    0.139878] ACPI: Power Resource [WRST] (off)
[    0.140040] ACPI: Power Resource [WRST] (off)
[    0.140210] ACPI: Power Resource [WRST] (off)
[    0.140369] ACPI: Power Resource [WRST] (off)
[    0.140524] ACPI: Power Resource [WRST] (off)
[    0.140682] ACPI: Power Resource [WRST] (off)
[    0.140841] ACPI: Power Resource [WRST] (off)
[    0.140998] ACPI: Power Resource [WRST] (off)
[    0.141157] ACPI: Power Resource [WRST] (off)
[    0.141505] ACPI: Power Resource [WRST] (off)
[    0.141684] ACPI: Power Resource [WRST] (off)
[    0.141841] ACPI: Power Resource [WRST] (off)
[    0.142000] ACPI: Power Resource [WRST] (off)
[    0.142156] ACPI: Power Resource [WRST] (off)
[    0.142318] ACPI: Power Resource [WRST] (off)
[    0.142474] ACPI: Power Resource [WRST] (off)
[    0.142631] ACPI: Power Resource [WRST] (off)
[    0.154766] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-fe])
[    0.154772] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.156406] acpi PNP0A08:00: _OSC: OS now controls [PCIeHotplug PME AER PCIeCapability]
[    0.156407] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
[    0.157003] PCI host bridge to bus 0000:00
[    0.157005] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[    0.157007] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.157008] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.157009] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000c3fff window]
[    0.157010] pci_bus 0000:00: root bus resource [mem 0x000c4000-0x000c7fff window]
[    0.157012] pci_bus 0000:00: root bus resource [mem 0x000c8000-0x000cbfff window]
[    0.157013] pci_bus 0000:00: root bus resource [mem 0x000cc000-0x000cffff window]
[    0.157014] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
[    0.157015] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
[    0.157017] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
[    0.157018] pci_bus 0000:00: root bus resource [mem 0x000dc000-0x000dffff window]
[    0.157019] pci_bus 0000:00: root bus resource [mem 0x000e0000-0x000e3fff window]
[    0.157020] pci_bus 0000:00: root bus resource [mem 0x000e4000-0x000e7fff window]
[    0.157022] pci_bus 0000:00: root bus resource [mem 0x000e8000-0x000ebfff window]
[    0.157023] pci_bus 0000:00: root bus resource [mem 0x000ec000-0x000effff window]
[    0.157024] pci_bus 0000:00: root bus resource [mem 0x8d000000-0xdfffffff window]
[    0.157025] pci_bus 0000:00: root bus resource [mem 0xfd000000-0xfe7fffff window]
[    0.157027] pci_bus 0000:00: root bus resource [bus 00-fe]
[    0.157037] pci 0000:00:00.0: [8086:1904] type 00 class 0x060000
[    0.157165] pci 0000:00:02.0: [8086:1916] type 00 class 0x030000
[    0.157177] pci 0000:00:02.0: reg 0x10: [mem 0xde000000-0xdeffffff 64bit]
[    0.157184] pci 0000:00:02.0: reg 0x18: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.157189] pci 0000:00:02.0: reg 0x20: [io  0xf000-0xf03f]
[    0.157324] pci 0000:00:04.0: [8086:1903] type 00 class 0x118000
[    0.157339] pci 0000:00:04.0: reg 0x10: [mem 0xdfb20000-0xdfb27fff 64bit]
[    0.157553] pci 0000:00:14.0: [8086:9d2f] type 00 class 0x0c0330
[    0.157578] pci 0000:00:14.0: reg 0x10: [mem 0xdfb10000-0xdfb1ffff 64bit]
[    0.157658] pci 0000:00:14.0: PME# supported from D3hot D3cold
[    0.157788] pci 0000:00:14.2: [8086:9d31] type 00 class 0x118000
[    0.157812] pci 0000:00:14.2: reg 0x10: [mem 0xdfb38000-0xdfb38fff 64bit]
[    0.158066] pci 0000:00:15.0: [8086:9d60] type 00 class 0x118000
[    0.158329] pci 0000:00:15.0: reg 0x10: [mem 0xdfb37000-0xdfb37fff 64bit]
[    0.159296] pci 0000:00:15.1: [8086:9d61] type 00 class 0x118000
[    0.159559] pci 0000:00:15.1: reg 0x10: [mem 0xdfb36000-0xdfb36fff 64bit]
[    0.160456] pci 0000:00:16.0: [8086:9d3a] type 00 class 0x078000
[    0.160485] pci 0000:00:16.0: reg 0x10: [mem 0xdfb35000-0xdfb35fff 64bit]
[    0.160569] pci 0000:00:16.0: PME# supported from D3hot
[    0.160708] pci 0000:00:17.0: [8086:9d03] type 00 class 0x010601
[    0.160729] pci 0000:00:17.0: reg 0x10: [mem 0xdfb30000-0xdfb31fff]
[    0.160737] pci 0000:00:17.0: reg 0x14: [mem 0xdfb34000-0xdfb340ff]
[    0.160746] pci 0000:00:17.0: reg 0x18: [io  0xf090-0xf097]
[    0.160754] pci 0000:00:17.0: reg 0x1c: [io  0xf080-0xf083]
[    0.160762] pci 0000:00:17.0: reg 0x20: [io  0xf060-0xf07f]
[    0.160771] pci 0000:00:17.0: reg 0x24: [mem 0xdfb33000-0xdfb337ff]
[    0.160820] pci 0000:00:17.0: PME# supported from D3hot
[    0.160960] pci 0000:00:1c.0: [8086:9d10] type 01 class 0x060400
[    0.161054] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[    0.161235] pci 0000:00:1c.7: [8086:9d17] type 01 class 0x060400
[    0.161328] pci 0000:00:1c.7: PME# supported from D0 D3hot D3cold
[    0.161496] pci 0000:00:1f.0: [8086:9d48] type 00 class 0x060100
[    0.161738] pci 0000:00:1f.2: [8086:9d21] type 00 class 0x058000
[    0.161755] pci 0000:00:1f.2: reg 0x10: [mem 0xdfb2c000-0xdfb2ffff]
[    0.161938] pci 0000:00:1f.3: [8086:9d70] type 00 class 0x040300
[    0.161969] pci 0000:00:1f.3: reg 0x10: [mem 0xdfb28000-0xdfb2bfff 64bit]
[    0.162004] pci 0000:00:1f.3: reg 0x20: [mem 0xdfb00000-0xdfb0ffff 64bit]
[    0.162062] pci 0000:00:1f.3: PME# supported from D3hot D3cold
[    0.162257] pci 0000:00:1f.4: [8086:9d23] type 00 class 0x0c0500
[    0.162319] pci 0000:00:1f.4: reg 0x10: [mem 0xdfb32000-0xdfb320ff 64bit]
[    0.162390] pci 0000:00:1f.4: reg 0x20: [io  0xf040-0xf05f]
[    0.162644] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.162648] pci 0000:00:1c.0:   bridge window [io  0xe000-0xefff]
[    0.162651] pci 0000:00:1c.0:   bridge window [mem 0xdf000000-0xdf9fffff]
[    0.162656] pci 0000:00:1c.0:   bridge window [mem 0xd0000000-0xd09fffff 64bit pref]
[    0.162976] pci 0000:02:00.0: [8086:095a] type 00 class 0x028000
[    0.163082] pci 0000:02:00.0: reg 0x10: [mem 0xdfa00000-0xdfa01fff 64bit]
[    0.163419] pci 0000:02:00.0: PME# supported from D0 D3hot D3cold
[    0.172225] pci 0000:00:1c.7: PCI bridge to [bus 02]
[    0.172230] pci 0000:00:1c.7:   bridge window [mem 0xdfa00000-0xdfafffff]
[    0.174526] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174590] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 *10 11 12 14 15)
[    0.174651] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174713] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174774] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174835] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174896] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.174957] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 *11 12 14 15)
[    0.175555] ACPI: EC: EC stopped
[    0.175556] ACPI: EC: EC started
[    0.175556] ACPI: EC: interrupt blocked
[    0.175757] ACPI: EC: interrupt unblocked
[    0.175777] ACPI: EC: event unblocked
[    0.175790] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0x50, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.175791] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot ECDT EC to handle transactions and events
[    0.175880] ACPI: \_SB_.PCI0.LPCB.EC0_: GPE=0x50, EC_CMD/EC_SC=0x66, EC_DATA=0x62
[    0.175882] ACPI: \_SB_.PCI0.LPCB.EC0_: Used as boot DSDT EC to handle transactions and events
[    0.176069] SCSI subsystem initialized
[    0.176096] libata version 3.00 loaded.
[    0.176096] pci 0000:00:02.0: vgaarb: setting as boot VGA device
[    0.176096] pci 0000:00:02.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.176096] pci 0000:00:02.0: vgaarb: bridge control possible
[    0.176096] vgaarb: loaded
[    0.176096] ACPI: bus type USB registered
[    0.176096] usbcore: registered new interface driver usbfs
[    0.176096] usbcore: registered new interface driver hub
[    0.176096] usbcore: registered new device driver usb
[    0.176096] EDAC MC: Ver: 3.0.0
[    0.176275] Registered efivars operations
[    0.180457] PCI: Using ACPI for IRQ routing
[    0.207958] PCI: pci_cache_line_size set to 64 bytes
[    0.208347] e820: reserve RAM buffer [mem 0x00058000-0x0005ffff]
[    0.208348] e820: reserve RAM buffer [mem 0x0009e000-0x0009ffff]
[    0.208349] e820: reserve RAM buffer [mem 0x825b4000-0x83ffffff]
[    0.208350] e820: reserve RAM buffer [mem 0x8519e000-0x87ffffff]
[    0.208352] e820: reserve RAM buffer [mem 0x86515000-0x87ffffff]
[    0.208353] e820: reserve RAM buffer [mem 0x87fff000-0x87ffffff]
[    0.208354] e820: reserve RAM buffer [mem 0x472000000-0x473ffffff]
[    0.208427] NetLabel: Initializing
[    0.208428] NetLabel:  domain hash size = 128
[    0.208429] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.208441] NetLabel:  unlabeled traffic allowed by default
[    0.208454] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[    0.208454] hpet0: 8 comparators, 64-bit 24.000000 MHz counter
[    0.210130] clocksource: Switched to clocksource hpet
[    0.216645] VFS: Disk quotas dquot_6.6.0
[    0.216661] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.216746] AppArmor: AppArmor Filesystem Enabled
[    0.216776] pnp: PnP ACPI init
[    0.217096] system 00:00: [io  0x0680-0x069f] has been reserved
[    0.217098] system 00:00: [io  0xffff] has been reserved
[    0.217099] system 00:00: [io  0xffff] has been reserved
[    0.217101] system 00:00: [io  0xffff] has been reserved
[    0.217102] system 00:00: [io  0x1800-0x18fe] has been reserved
[    0.217104] system 00:00: [io  0x164e-0x164f] has been reserved
[    0.217107] system 00:00: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217206] pnp 00:01: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.217239] system 00:02: [io  0x1854-0x1857] has been reserved
[    0.217242] system 00:02: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
[    0.217363] system 00:03: [io  0x0240-0x0259] has been reserved
[    0.217365] system 00:03: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217403] pnp 00:04: Plug and Play ACPI device, IDs ATK3001 PNP030b (active)
[    0.217561] system 00:05: [mem 0xfed10000-0xfed17fff] has been reserved
[    0.217562] system 00:05: [mem 0xfed18000-0xfed18fff] has been reserved
[    0.217564] system 00:05: [mem 0xfed19000-0xfed19fff] has been reserved
[    0.217565] system 00:05: [mem 0xe0000000-0xefffffff] has been reserved
[    0.217567] system 00:05: [mem 0xfed20000-0xfed3ffff] has been reserved
[    0.217569] system 00:05: [mem 0xfed90000-0xfed93fff] could not be reserved
[    0.217570] system 00:05: [mem 0xfed45000-0xfed8ffff] has been reserved
[    0.217572] system 00:05: [mem 0xff000000-0xffffffff] has been reserved
[    0.217573] system 00:05: [mem 0xfee00000-0xfeefffff] could not be reserved
[    0.217575] system 00:05: [mem 0xdffe0000-0xdfffffff] has been reserved
[    0.217577] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217612] system 00:06: [mem 0xfd000000-0xfdabffff] has been reserved
[    0.217614] system 00:06: [mem 0xfdad0000-0xfdadffff] has been reserved
[    0.217615] system 00:06: [mem 0xfdb00000-0xfdffffff] has been reserved
[    0.217617] system 00:06: [mem 0xfe000000-0xfe01ffff] could not be reserved
[    0.217618] system 00:06: [mem 0xfe036000-0xfe03bfff] has been reserved
[    0.217620] system 00:06: [mem 0xfe03d000-0xfe3fffff] has been reserved
[    0.217621] system 00:06: [mem 0xfe410000-0xfe7fffff] has been reserved
[    0.217623] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.217937] system 00:07: [io  0xff00-0xfffe] has been reserved
[    0.217939] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.219136] system 00:08: [mem 0xfdaf0000-0xfdafffff] has been reserved
[    0.219138] system 00:08: [mem 0xfdae0000-0xfdaeffff] has been reserved
[    0.219139] system 00:08: [mem 0xfdac0000-0xfdacffff] has been reserved
[    0.219141] system 00:08: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.220091] pnp: PnP ACPI: found 9 devices
[    0.228031] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.228057] pci 0000:00:1c.0: PCI bridge to [bus 01]
[    0.228065] pci 0000:00:1c.0:   bridge window [io  0xe000-0xefff]
[    0.228069] pci 0000:00:1c.0:   bridge window [mem 0xdf000000-0xdf9fffff]
[    0.228072] pci 0000:00:1c.0:   bridge window [mem 0xd0000000-0xd09fffff 64bit pref]
[    0.228077] pci 0000:00:1c.7: PCI bridge to [bus 02]
[    0.228083] pci 0000:00:1c.7:   bridge window [mem 0xdfa00000-0xdfafffff]
[    0.228091] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[    0.228092] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
[    0.228094] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[    0.228095] pci_bus 0000:00: resource 7 [mem 0x000c0000-0x000c3fff window]
[    0.228096] pci_bus 0000:00: resource 8 [mem 0x000c4000-0x000c7fff window]
[    0.228097] pci_bus 0000:00: resource 9 [mem 0x000c8000-0x000cbfff window]
[    0.228099] pci_bus 0000:00: resource 10 [mem 0x000cc000-0x000cffff window]
[    0.228100] pci_bus 0000:00: resource 11 [mem 0x000d0000-0x000d3fff window]
[    0.228101] pci_bus 0000:00: resource 12 [mem 0x000d4000-0x000d7fff window]
[    0.228103] pci_bus 0000:00: resource 13 [mem 0x000d8000-0x000dbfff window]
[    0.228104] pci_bus 0000:00: resource 14 [mem 0x000dc000-0x000dffff window]
[    0.228105] pci_bus 0000:00: resource 15 [mem 0x000e0000-0x000e3fff window]
[    0.228107] pci_bus 0000:00: resource 16 [mem 0x000e4000-0x000e7fff window]
[    0.228108] pci_bus 0000:00: resource 17 [mem 0x000e8000-0x000ebfff window]
[    0.228109] pci_bus 0000:00: resource 18 [mem 0x000ec000-0x000effff window]
[    0.228110] pci_bus 0000:00: resource 19 [mem 0x8d000000-0xdfffffff window]
[    0.228112] pci_bus 0000:00: resource 20 [mem 0xfd000000-0xfe7fffff window]
[    0.228113] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.228115] pci_bus 0000:01: resource 1 [mem 0xdf000000-0xdf9fffff]
[    0.228116] pci_bus 0000:01: resource 2 [mem 0xd0000000-0xd09fffff 64bit pref]
[    0.228117] pci_bus 0000:02: resource 1 [mem 0xdfa00000-0xdfafffff]
[    0.228253] NET: Registered protocol family 2
[    0.228401] TCP established hash table entries: 131072 (order: 8, 1048576 bytes)
[    0.228576] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.228688] TCP: Hash tables configured (established 131072 bind 65536)
[    0.228718] UDP hash table entries: 8192 (order: 6, 262144 bytes)
[    0.228756] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes)
[    0.228812] NET: Registered protocol family 1
[    0.228826] pci 0000:00:02.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.229517] PCI: CLS 0 bytes, default 64
[    0.229546] Unpacking initramfs...
[    0.947134] Freeing initrd memory: 48212K
[    0.947200] DMAR: ACPI device "device:6a" under DMAR at fed91000 as 00:15.0
[    0.947203] DMAR: ACPI device "device:6b" under DMAR at fed91000 as 00:15.1
[    0.947217] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.947220] software IO TLB [mem 0x7d57f000-0x8157f000] (64MB) mapped at [ffff8a1dfd57f000-ffff8a1e0157efff]
[    0.947414] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x255cb6cc5db, max_idle_ns: 440795203504 ns
[    0.947537] Scanning for low memory corruption every 60 seconds
[    0.947882] audit: initializing netlink subsys (disabled)
[    0.947963] audit: type=2000 audit(1519512093.947:1): state=initialized audit_enabled=0 res=1
[    0.948323] Initialise system trusted keyrings
[    0.948330] Key type blacklist registered
[    0.948396] workingset: timestamp_bits=36 max_order=22 bucket_order=0
[    0.949346] zbud: loaded
[    0.949840] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.950005] fuse init (API version 7.26)
[    0.952652] Key type asymmetric registered
[    0.952653] Asymmetric key parser 'x509' registered
[    0.952681] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
[    0.952743] io scheduler noop registered
[    0.952744] io scheduler deadline registered
[    0.952766] io scheduler cfq registered (default)
[    0.953433] pcieport 0000:00:1c.0: AER enabled with IRQ 122
[    0.953456] pcieport 0000:00:1c.7: AER enabled with IRQ 123
[    0.953472] pcieport 0000:00:1c.0: Signaling PME with IRQ 122
[    0.953483] pcieport 0000:00:1c.7: Signaling PME with IRQ 123
[    0.953504] pciehp 0000:00:1c.0:pcie004: Slot #4 AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug+ Surprise+ Interlock- NoCompl+ LLActRep+
[    0.953579] efifb: probing for efifb
[    0.953589] efifb: framebuffer at 0xc0000000, using 1920k, total 1920k
[    0.953590] efifb: mode is 800x600x32, linelength=3200, pages=1
[    0.953590] efifb: scrolling: redraw
[    0.953592] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    0.953684] Console: switching to colour frame buffer device 100x37
[    0.953694] fb0: EFI VGA frame buffer device
[    0.953698] intel_idle: MWAIT substates: 0x11142120
[    0.953699] intel_idle: v0.4.1 model 0x4E
[    0.953918] intel_idle: lapic_timer_reliable_states 0xffffffff
[    0.954057] ACPI: AC Adapter [AC0] (off-line)
[    0.955332] input: Lid Switch as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0D:00/input/input0
[    0.956570] ACPI: Lid Switch [LID]
[    0.956597] input: Sleep Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0E:00/input/input1
[    0.956659] ACPI: Sleep Button [SLPB]
[    0.956688] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input2
[    0.956740] ACPI: Power Button [PWRF]
[    0.958045] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    0.958161] thermal LNXTHERM:00: registered as thermal_zone0
[    0.958162] ACPI: Thermal Zone [THRM] (31 C)
[    0.958195] GHES: HEST is not enabled!
[    0.958295] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.962967] Linux agpgart interface v0.103
[    0.967570] ACPI: Battery Slot [BAT0] (battery present)
[    0.969430] loop: module loaded
[    0.969553] libphy: Fixed MDIO Bus: probed
[    0.969554] tun: Universal TUN/TAP device driver, 1.6
[    0.969608] PPP generic driver version 2.4.2
[    0.969667] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.969669] ehci-pci: EHCI PCI platform driver
[    0.969677] ehci-platform: EHCI generic platform driver
[    0.969684] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.969685] ohci-pci: OHCI PCI platform driver
[    0.969691] ohci-platform: OHCI generic platform driver
[    0.969696] uhci_hcd: USB Universal Host Controller Interface driver
[    0.969853] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.969857] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
[    0.970962] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x00109810
[    0.970967] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[    0.971051] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.971052] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.971054] usb usb1: Product: xHCI Host Controller
[    0.971055] usb usb1: Manufacturer: Linux 4.13.0-36-generic xhci-hcd
[    0.971056] usb usb1: SerialNumber: 0000:00:14.0
[    0.971167] hub 1-0:1.0: USB hub found
[    0.971187] hub 1-0:1.0: 12 ports detected
[    0.971790] xhci_hcd 0000:00:14.0: xHCI Host Controller
[    0.971793] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[    0.971829] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003
[    0.971830] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.971831] usb usb2: Product: xHCI Host Controller
[    0.971833] usb usb2: Manufacturer: Linux 4.13.0-36-generic xhci-hcd
[    0.971834] usb usb2: SerialNumber: 0000:00:14.0
[    0.971934] hub 2-0:1.0: USB hub found
[    0.971949] hub 2-0:1.0: 6 ports detected
[    0.972843] i8042: PNP: PS/2 Controller [PNP030b:PS2K] at 0x60,0x64 irq 1
[    0.972844] i8042: PNP: PS/2 appears to have AUX port disabled, if this is incorrect please boot with i8042.nopnp
[    0.974895] serio: i8042 KBD port at 0x60,0x64 irq 1
[    0.975030] mousedev: PS/2 mouse device common for all mice
[    0.975265] rtc_cmos 00:01: RTC can wake from S4
[    0.975664] rtc_cmos 00:01: rtc core: registered rtc_cmos as rtc0
[    0.975749] rtc_cmos 00:01: alarms up to one month, y3k, 242 bytes nvram, hpet irqs
[    0.975754] i2c /dev entries driver
[    0.975790] device-mapper: uevent: version 1.0.3
[    0.975862] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    0.975865] intel_pstate: Intel P-state driver initializing
[    0.976566] intel_pstate: HWP enabled
[    0.976749] ledtrig-cpu: registered to indicate activity on CPUs
[    0.976751] EFI Variables Facility v0.08 2004-May-17
[    0.982128] NET: Registered protocol family 10
[    0.986848] Segment Routing with IPv6
[    0.986867] NET: Registered protocol family 17
[    0.986873] Key type dns_resolver registered
[    0.987613] RAS: Correctable Errors collector initialized.
[    0.987692] microcode: sig=0x406e3, pf=0x80, revision=0x84
[    0.987795] microcode: Microcode Update Driver: v2.2.
[    0.987896] sched_clock: Marking stable (987792532, 0)->(1095725485, -107932953)
[    0.988212] registered taskstats version 1
[    0.988218] Loading compiled-in X.509 certificates
[    0.990149] Loaded X.509 cert 'Build time autogenerated kernel key: 6392960b5d1a7feefef54e83c93c27dba99187fc'
[    0.992105] Loaded UEFI:db cert 'ASUSTeK Notebook SW Key Certificate: b8e581e4df77a5bb4282d5ccfc00c071' linked to secondary sys keyring
[    0.992272] Loaded UEFI:db cert 'ASUSTeK MotherBoard SW Key Certificate: da83b990422ebc8c441f8d8b039a65a2' linked to secondary sys keyring
[    0.992291] Loaded UEFI:db cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4' linked to secondary sys keyring
[    0.992306] Loaded UEFI:db cert 'Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53' linked to secondary sys keyring
[    0.992472] Loaded UEFI:db cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63' linked to secondary sys keyring
[    0.992774] Loaded UEFI:MokListRT cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63' linked to secondary sys keyring
[    0.993084] zswap: loaded using pool lzo/zbud
[    0.997601] Key type big_key registered
[    0.997603] Key type trusted registered
[    0.999635] Key type encrypted registered
[    0.999638] AppArmor: AppArmor sha1 policy hashing enabled
[    0.999644] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    0.999656] evm: HMAC attrs: 0x1
[    1.000740]   Magic number: 6:247:705
[    1.001023] rtc_cmos 00:01: setting system clock to 2018-02-24 22:41:34 UTC (1519512094)
[    1.001088] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    1.001088] EDD information not available.
[    1.001118] PM: Hibernation image not present or could not be loaded.
[    1.002673] Freeing unused kernel memory: 2364K
[    1.002673] Write protecting the kernel read-only data: 18432k
[    1.003154] Freeing unused kernel memory: 2024K
[    1.003374] Freeing unused kernel memory: 88K
[    1.004797] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.004798] x86/mm: Checking user space page tables
[    1.006028] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.014598] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input3
[    1.116777] hidraw: raw HID events driver (C) Jiri Kosina
[    1.117892] ahci 0000:00:17.0: version 3.0
[    1.118195] ahci 0000:00:17.0: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x5 impl SATA mode
[    1.118197] ahci 0000:00:17.0: flags: 64bit ncq pm led clo only pio slum part deso sadm sds apst 
[    1.118574] scsi host0: ahci
[    1.119043] scsi host1: ahci
[    1.119163] scsi host2: ahci
[    1.119218] ata1: SATA max UDMA/133 abar m2048@0xdfb33000 port 0xdfb33100 irq 125
[    1.119218] ata2: DUMMY
[    1.119221] ata3: SATA max UDMA/133 abar m2048@0xdfb33000 port 0xdfb33200 irq 125
[    1.146610] [drm] Memory usable by graphics device = 4096M
[    1.146612] checking generic (c0000000 1e0000) vs hw (c0000000 10000000)
[    1.146613] fb: switching to inteldrmfb from EFI VGA
[    1.146630] Console: switching to colour dummy device 80x25
[    1.146716] [drm] Replacing VGA console driver
[    1.152183] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.152184] [drm] Driver supports precise vblank timestamp query.
[    1.160822] [drm] Finished loading DMC firmware i915/skl_dmc_ver1_26.bin (v1.26)
[    1.161963] i915 0000:00:02.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=io+mem
[    1.170228] [drm] Initialized i915 1.6.0 20170619 for 0000:00:02.0 on minor 0
[    1.172252] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[    1.174621] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input4
[    1.296123] usb 1-6: new high-speed USB device number 2 using xhci_hcd
[    1.433169] ata3: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.433344] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.434681] ata3.00: ATA-9: SanDisk SD8SNAT256G1002, Z2317002, max UDMA/133
[    1.434682] ata3.00: 500118192 sectors, multi 1: LBA48 NCQ (depth 31/32), AA
[    1.435008] ata1.00: supports DRM functions and may not be fully accessible
[    1.435854] ata1.00: disabling queued TRIM support
[    1.435855] ata1.00: ATA-9: Samsung SSD 850 EVO 500GB, EMT02B6Q, max UDMA/133
[    1.435856] ata1.00: 976773168 sectors, multi 1: LBA48 NCQ (depth 31/32), AA
[    1.438151] ata1.00: supports DRM functions and may not be fully accessible
[    1.438947] ata1.00: disabling queued TRIM support
[    1.440744] ata1.00: configured for UDMA/133
[    1.441481] scsi 0:0:0:0: Direct-Access     ATA      Samsung SSD 850  2B6Q PQ: 0 ANSI: 5
[    1.442510] ata3.00: configured for UDMA/133
[    1.487145] usb 1-6: New USB device found, idVendor=04f2, idProduct=b57a
[    1.487147] usb 1-6: New USB device strings: Mfr=3, Product=1, SerialNumber=2
[    1.487149] usb 1-6: Product: USB2.0 HD UVC WebCam
[    1.487150] usb 1-6: Manufacturer: Chicony Electronics Co.,Ltd.
[    1.487151] usb 1-6: SerialNumber: 0x0001
[    1.496341] sd 0:0:0:0: [sda] 976773168 512-byte logical blocks: (500 GB/466 GiB)
[    1.496355] sd 0:0:0:0: [sda] Write Protect is off
[    1.496357] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    1.496371] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    1.496373] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.496660] scsi 2:0:0:0: Direct-Access     ATA      SanDisk SD8SNAT2 7002 PQ: 0 ANSI: 5
[    1.498623]  sda: sda1 sda2
[    1.499709] sd 0:0:0:0: [sda] supports TCG Opal
[    1.499710] sd 0:0:0:0: [sda] Attached SCSI disk
[    1.544372] sd 2:0:0:0: Attached scsi generic sg1 type 0
[    1.544814] sd 2:0:0:0: [sdb] 500118192 512-byte logical blocks: (256 GB/238 GiB)
[    1.544886] sd 2:0:0:0: [sdb] Write Protect is off
[    1.544888] sd 2:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[    1.544989] sd 2:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.549696]  sdb: sdb1 sdb2 sdb3
[    1.551368] sd 2:0:0:0: [sdb] Attached SCSI disk
[    1.562322] fbcon: inteldrmfb (fb0) is primary device
[    1.562391] Console: switching to colour frame buffer device 240x67
[    1.562415] i915 0000:00:02.0: fb0: inteldrmfb frame buffer device
[    1.668037] usb 1-8: new full-speed USB device number 3 using xhci_hcd
[    1.679523] EXT4-fs (sdb2): mounted filesystem with ordered data mode. Opts: (null)
[    1.810500] usb 1-8: New USB device found, idVendor=8087, idProduct=0a2a
[    1.810502] usb 1-8: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.887542] systemd[1]: systemd 229 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN)
[    1.887675] systemd[1]: Detected architecture x86-64.
[    1.887974] systemd[1]: Set hostname to <wispDev>.
[    1.952342] clocksource: Switched to clocksource tsc
[    2.013750] systemd[1]: Created slice System Slice.
[    2.013922] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[    2.013956] systemd[1]: Listening on Journal Socket (/dev/log).
[    2.013965] systemd[1]: Reached target User and Group Name Lookups.
[    2.013995] systemd[1]: Started Trigger resolvconf update for networkd DNS.
[    2.014013] systemd[1]: Listening on Syslog Socket.
[    2.014060] systemd[1]: Listening on Journal Audit Socket.
[    2.077496] lp: driver loaded but no devices found
[    2.089413] ppdev: user-space parallel port driver
[    2.196712] EXT4-fs (sdb2): re-mounted. Opts: errors=remount-ro
[    2.210299] systemd-journald[252]: Received request to flush runtime journal from PID 1
[    2.270849] input: Asus Wireless Radio Control as /devices/LNXSYSTM:00/LNXSYBUS:00/ATK4002:00/input/input5
[    2.291634] tpm_crb MSFT0101:00: [Firmware Bug]: ACPI region does not cover the entire command/response buffer. [mem 0xfed40000-0xfed4087f flags 0x200] vs fed40080 f80
[    2.291643] tpm_crb MSFT0101:00: [Firmware Bug]: ACPI region does not cover the entire command/response buffer. [mem 0xfed40000-0xfed4087f flags 0x200] vs fed40080 f80
[    2.300041] Bluetooth: Core ver 2.22
[    2.300054] NET: Registered protocol family 31
[    2.300055] Bluetooth: HCI device and connection manager initialized
[    2.300058] Bluetooth: HCI socket layer initialized
[    2.300060] Bluetooth: L2CAP socket layer initialized
[    2.300064] Bluetooth: SCO socket layer initialized
[    2.323758] Bluetooth: HCI UART driver ver 2.3
[    2.323760] Bluetooth: HCI UART protocol H4 registered
[    2.323760] Bluetooth: HCI UART protocol BCSP registered
[    2.323774] Bluetooth: HCI UART protocol LL registered
[    2.323775] Bluetooth: HCI UART protocol ATH3K registered
[    2.323776] Bluetooth: HCI UART protocol Three-wire (H5) registered
[    2.323799] Bluetooth: HCI UART protocol Intel registered
[    2.323812] Bluetooth: HCI UART protocol Broadcom registered
[    2.323813] Bluetooth: HCI UART protocol QCA registered
[    2.323813] Bluetooth: HCI UART protocol AG6XX registered
[    2.323814] Bluetooth: HCI UART protocol Marvell registered
[    2.356775] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    2.360888] mei_me 0000:00:16.0: enabling device (0000 -> 0002)
[    2.365959] intel-lpss 0000:00:15.0: enabling device (0000 -> 0002)
[    2.373558] usbcore: registered new interface driver btusb
[    2.380693] idma64 idma64.0: Found Intel integrated DMA 64-bit
[    2.385874] intel-lpss 0000:00:15.1: enabling device (0000 -> 0002)
[    2.386135] idma64 idma64.1: Found Intel integrated DMA 64-bit
[    2.386955] asus_wmi: ASUS WMI generic driver loaded
[    2.389042] Bluetooth: hci0: read Intel version: 370810011003110e00
[    2.391652] i2c_hid i2c-ELAN1200:00: i2c-ELAN1200:00 supply vdd not found, using dummy regulator
[    2.391681] asus_wmi: Initialization: 0x1
[    2.391721] asus_wmi: BIOS WMI version: 7.9
[    2.391782] asus_wmi: SFUN value: 0xa2065
[    2.393355] input: Asus WMI hotkeys as /devices/platform/asus-nb-wmi/input/input6
[    2.395787] asus_wmi: Number of fans: 1
[    2.413522] Bluetooth: hci0: Intel Bluetooth firmware file: intel/ibt-hw-37.8.10-fw-1.10.3.11.e.bseq
[    2.417101] RAPL PMU: API unit is 2^-32 Joules, 5 fixed counters, 655360 ms ovfl timer
[    2.417102] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
[    2.417103] RAPL PMU: hw unit of domain package 2^-14 Joules
[    2.417104] RAPL PMU: hw unit of domain dram 2^-14 Joules
[    2.417105] RAPL PMU: hw unit of domain pp1-gpu 2^-14 Joules
[    2.417105] RAPL PMU: hw unit of domain psys 2^-14 Joules
[    2.420223] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    2.427557] media: Linux media interface: v0.10
[    2.446086] AVX2 version of gcm_enc/dec engaged.
[    2.446087] AES CTR mode by8 optimization enabled
[    2.448099] Linux video capture interface: v2.00
[    2.471933] uvcvideo: Found UVC 1.00 device USB2.0 HD UVC WebCam (04f2:b57a)
[    2.476151] uvcvideo 1-6:1.0: Entity type for entity Realtek Extended Controls Unit was not initialized!
[    2.476154] uvcvideo 1-6:1.0: Entity type for entity Extension 4 was not initialized!
[    2.476155] uvcvideo 1-6:1.0: Entity type for entity Processing 2 was not initialized!
[    2.476157] uvcvideo 1-6:1.0: Entity type for entity Camera 1 was not initialized!
[    2.476221] input: USB2.0 HD UVC WebCam: USB2.0 HD as /devices/pci0000:00/0000:00:14.0/usb1/1-6/1-6:1.0/input/input7
[    2.476276] usbcore: registered new interface driver uvcvideo
[    2.476276] USB Video Class driver (1.1.1)
[    2.481679] Intel(R) Wireless WiFi driver for Linux
[    2.481680] Copyright(c) 2003- 2015 Intel Corporation
[    2.489962] iwlwifi 0000:02:00.0: loaded firmware version 29.610311.0 op_mode iwlmvm
[    2.518559] iwlwifi 0000:02:00.0: Detected Intel(R) Dual Band Wireless AC 7265, REV=0x210
[    2.538935] iwlwifi 0000:02:00.0: base HW address: a4:02:b9:82:12:43
[    2.573464] intel_rapl: Found RAPL domain package
[    2.573465] intel_rapl: Found RAPL domain core
[    2.573466] intel_rapl: Found RAPL domain uncore
[    2.573467] intel_rapl: Found RAPL domain dram
[    2.612647] ieee80211 phy0: Selected rate control algorithm 'iwl-mvm-rs'
[    2.612885] (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
[    2.612901] thermal thermal_zone9: failed to read out thermal zone (-5)
[    2.654857] hid-multitouch 0018:04F3:3022.0001: Ignoring the extra HID_DG_INPUTMODE
[    2.654921] input: ELAN1200:00 04F3:3022 Touchpad as /devices/pci0000:00/0000:00:15.1/i2c_designware.1/i2c-6/i2c-ELAN1200:00/0018:04F3:3022.0001/input/input9
[    2.655885] hid-multitouch 0018:04F3:3022.0001: input,hidraw0: I2C HID v1.00 Mouse [ELAN1200:00 04F3:3022] on i2c-ELAN1200:00
[    2.673380] iwlwifi 0000:02:00.0 wlp2s0: renamed from wlan0
[    2.681327] Adding 16637948k swap on /dev/sdb3.  Priority:-1 extents:1 across:16637948k SSFS
[    2.709114] Bluetooth: hci0: Intel Bluetooth firmware patch completed and activated
[    2.816261] [drm] RC6 on
[    3.714623] snd_hda_intel 0000:00:1f.3: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
[    3.740241] snd_hda_codec_generic hdaudioC0D0: autoconfig for Generic: line_outs=1 (0x17/0x0/0x0/0x0/0x0) type:speaker
[    3.740243] snd_hda_codec_generic hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[    3.740244] snd_hda_codec_generic hdaudioC0D0:    hp_outs=1 (0x16/0x0/0x0/0x0/0x0)
[    3.740245] snd_hda_codec_generic hdaudioC0D0:    mono: mono_out=0x0
[    3.740246] snd_hda_codec_generic hdaudioC0D0:    inputs:
[    3.740247] snd_hda_codec_generic hdaudioC0D0:      Internal Mic=0x1a
[    3.740248] snd_hda_codec_generic hdaudioC0D0:      Mic=0x19
[    3.750660] input: HDA Intel PCH Mic as /devices/pci0000:00/0000:00:1f.3/sound/card0/input10
[    3.750715] input: HDA Intel PCH Headphone as /devices/pci0000:00/0000:00:1f.3/sound/card0/input11
[    3.750768] input: HDA Intel PCH HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input12
[    3.750839] input: HDA Intel PCH HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input13
[    3.750904] input: HDA Intel PCH HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input14
[    3.750956] input: HDA Intel PCH HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input15
[    3.751002] input: HDA Intel PCH HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:1f.3/sound/card0/input16
[    3.772800] random: crng init done
[    4.187839] audit: type=1400 audit(1519512097.686:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=755 comm="apparmor_parser"
[    4.187843] audit: type=1400 audit(1519512097.686:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=755 comm="apparmor_parser"
[    4.187845] audit: type=1400 audit(1519512097.686:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=755 comm="apparmor_parser"
[    4.187847] audit: type=1400 audit(1519512097.686:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=755 comm="apparmor_parser"
[    4.192487] audit: type=1400 audit(1519512097.691:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session" pid=754 comm="apparmor_parser"
[    4.192490] audit: type=1400 audit(1519512097.691:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session//chromium" pid=754 comm="apparmor_parser"
[    4.201947] audit: type=1400 audit(1519512097.701:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="webbrowser-app" pid=758 comm="apparmor_parser"
[    4.201950] audit: type=1400 audit(1519512097.701:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="webbrowser-app//oxide_helper" pid=758 comm="apparmor_parser"
[    4.203340] audit: type=1400 audit(1519512097.702:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=759 comm="apparmor_parser"
[    4.324714] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[    4.324715] Bluetooth: BNEP filters: protocol multicast
[    4.324718] Bluetooth: BNEP socket layer initialized
[    4.783079] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[    4.925675] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[    5.023672] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[    5.070636] Guest personality initialized and is inactive
[    5.070673] VMCI host device registered (name=vmci, major=10, minor=54)
[    5.070674] Initialized host personality
[    5.117660] NET: Registered protocol family 40
[    5.948057] NET: Unregistered protocol family 40
[    6.634252] Bluetooth: RFCOMM TTY layer initialized
[    6.634256] Bluetooth: RFCOMM socket layer initialized
[    6.634260] Bluetooth: RFCOMM ver 1.11
[   11.904772] wlp2s0: authenticate with 88:ad:43:b9:2d:a8
[   11.910624] wlp2s0: send auth to 88:ad:43:b9:2d:a8 (try 1/3)
[   11.913341] wlp2s0: authenticated
[   11.916024] wlp2s0: associate with 88:ad:43:b9:2d:a8 (try 1/3)
[   11.928836] wlp2s0: RX AssocResp from 88:ad:43:b9:2d:a8 (capab=0x411 status=0 aid=1)
[   11.930532] wlp2s0: associated
[   11.930572] IPv6: ADDRCONF(NETDEV_CHANGE): wlp2s0: link becomes ready
[   12.001717] wlp2s0: Limiting TX power to 14 (17 - 3) dBm as advertised by 88:ad:43:b9:2d:a8
[   13.928512] vmmon: loading out-of-tree module taints kernel.
[   13.928562] vmmon: module verification failed: signature and/or required key missing - tainting kernel
[   13.929343] /dev/vmmon[3143]: Module vmmon: registered with major=10 minor=165
[   13.929345] /dev/vmmon[3143]: Using tsc_khz as TSC frequency: 2592000
[   13.929346] /dev/vmmon[3143]: Module vmmon: initialized
[   13.942494] Guest personality initialized and is inactive
[   13.942791] VMCI host device registered (name=vmci, major=10, minor=54)
[   13.942792] Initialized host personality
[   13.960443] NET: Registered protocol family 40
[   14.047694] /dev/vmnet: open called by PID 3260 (vmnet-bridge)
[   14.047698] /dev/vmnet: hub 0 does not exist, allocating memory.
[   14.047717] /dev/vmnet: port on hub 0 successfully opened
[   14.047724] bridge-wlp2s0: device is wireless, enabling SMAC
[   14.047726] bridge-wlp2s0: up
[   14.047729] bridge-wlp2s0: attached
[   15.064107] /dev/vmnet: open called by PID 3430 (vmnet-netifup)
[   15.064111] /dev/vmnet: hub 1 does not exist, allocating memory.
[   15.064124] /dev/vmnet: port on hub 1 successfully opened
[   15.090087] /dev/vmnet: open called by PID 3432 (vmnet-dhcpd)
[   15.090095] /dev/vmnet: port on hub 1 successfully opened
[   15.110927] /dev/vmnet: open called by PID 3457 (vmnet-natd)
[   15.110932] /dev/vmnet: hub 8 does not exist, allocating memory.
[   15.110952] /dev/vmnet: port on hub 8 successfully opened
[   15.112098] userif-3: sent link down event.
[   15.112100] userif-3: sent link up event.
[   15.114083] /dev/vmnet: open called by PID 3459 (vmnet-netifup)
[   15.114092] /dev/vmnet: port on hub 8 successfully opened
[   15.132276] /dev/vmnet: open called by PID 3466 (vmnet-dhcpd)
[   15.132284] /dev/vmnet: port on hub 8 successfully opened
[  103.537421] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[  103.537433] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[  103.537437] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[  103.537439] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[  147.057666] asus_wmi: Unknown key cf pressed
[  523.790092] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[  523.790122] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[  523.790144] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[  523.790159] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 1254.016417] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 1254.016445] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 1254.016474] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 1254.016478] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 1617.645195] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 1617.645220] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 1617.645237] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 1617.645248] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 2344.904744] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 2344.904812] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 2344.904833] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 2344.904845] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 2429.795677] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 2429.795701] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 2429.795718] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 2429.795730] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4002.397679] iwlwifi 0000:02:00.0: Microcode SW error detected.  Restarting 0x2000000.
[ 4002.397812] iwlwifi 0000:02:00.0: Start IWL Error Log Dump:
[ 4002.397815] iwlwifi 0000:02:00.0: Status: 0x00000200, count: 6
[ 4002.397818] iwlwifi 0000:02:00.0: Loaded firmware version: 29.610311.0
[ 4002.397820] iwlwifi 0000:02:00.0: 0x0000105C | ADVANCED_SYSASSERT          
[ 4002.397822] iwlwifi 0000:02:00.0: 0x00000220 | trm_hw_status0
[ 4002.397825] iwlwifi 0000:02:00.0: 0x00000000 | trm_hw_status1
[ 4002.397827] iwlwifi 0000:02:00.0: 0x00043D58 | branchlink2
[ 4002.397829] iwlwifi 0000:02:00.0: 0x0004B016 | interruptlink1
[ 4002.397831] iwlwifi 0000:02:00.0: 0x00000000 | interruptlink2
[ 4002.397833] iwlwifi 0000:02:00.0: 0xDEADBEEF | data1
[ 4002.397836] iwlwifi 0000:02:00.0: 0xDEADBEEF | data2
[ 4002.397838] iwlwifi 0000:02:00.0: 0xDEADBEEF | data3
[ 4002.397840] iwlwifi 0000:02:00.0: 0x0E017A98 | beacon time
[ 4002.397842] iwlwifi 0000:02:00.0: 0x3186A56B | tsf low
[ 4002.397844] iwlwifi 0000:02:00.0: 0x0000002B | tsf hi
[ 4002.397845] iwlwifi 0000:02:00.0: 0x00000000 | time gp1
[ 4002.397847] iwlwifi 0000:02:00.0: 0xEE458B6C | time gp2
[ 4002.397849] iwlwifi 0000:02:00.0: 0x00000001 | uCode revision type
[ 4002.397851] iwlwifi 0000:02:00.0: 0x0000001D | uCode version major
[ 4002.397853] iwlwifi 0000:02:00.0: 0x00095007 | uCode version minor
[ 4002.397855] iwlwifi 0000:02:00.0: 0x00000210 | hw version
[ 4002.397857] iwlwifi 0000:02:00.0: 0x00489200 | board version
[ 4002.397859] iwlwifi 0000:02:00.0: 0x0A04001C | hcmd
[ 4002.397861] iwlwifi 0000:02:00.0: 0x24022002 | isr0
[ 4002.397863] iwlwifi 0000:02:00.0: 0x00800000 | isr1
[ 4002.397865] iwlwifi 0000:02:00.0: 0x00000002 | isr2
[ 4002.397867] iwlwifi 0000:02:00.0: 0x00417CC1 | isr3
[ 4002.397869] iwlwifi 0000:02:00.0: 0x00000000 | isr4
[ 4002.397871] iwlwifi 0000:02:00.0: 0x0A03001C | last cmd Id
[ 4002.397873] iwlwifi 0000:02:00.0: 0x00000000 | wait_event
[ 4002.397875] iwlwifi 0000:02:00.0: 0x000000D4 | l2p_control
[ 4002.397877] iwlwifi 0000:02:00.0: 0x00018030 | l2p_duration
[ 4002.397879] iwlwifi 0000:02:00.0: 0x00000007 | l2p_mhvalid
[ 4002.397881] iwlwifi 0000:02:00.0: 0x00000081 | l2p_addr_match
[ 4002.397884] iwlwifi 0000:02:00.0: 0x00000005 | lmpm_pmg_sel
[ 4002.397886] iwlwifi 0000:02:00.0: 0x29102230 | timestamp
[ 4002.397888] iwlwifi 0000:02:00.0: 0x00003848 | flow_handler
[ 4002.397891] ieee80211 phy0: Hardware restart was requested
[ 4002.540189] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4002.540194] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4002.540197] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4002.540200] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4002.620245] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4002.620268] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4002.620289] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4002.620304] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4141.745673] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4141.745685] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4141.745689] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4141.745693] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4332.626563] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4332.626587] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4332.626604] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4332.626615] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 4984.107737] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 4984.107762] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 4984.107778] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 4984.107790] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 5295.457653] pcieport 0000:00:1c.7: AER: Corrected error received: id=00e7
[ 5295.457664] pcieport 0000:00:1c.7: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e7(Receiver ID)
[ 5295.457668] pcieport 0000:00:1c.7:   device [8086:9d17] error status/mask=00000001/00002000
[ 5295.457670] pcieport 0000:00:1c.7:    [ 0] Receiver Error         (First)
[ 5883.291541] wlp2s0: deauthenticating from 88:ad:43:b9:2d:a8 by local choice (Reason: 3=DEAUTH_LEAVING)
[ 5883.307015] wlp2s0: failed to remove key (1, ff:ff:ff:ff:ff:ff) from hardware (-22)
[ 5883.307196] wlp2s0: failed to remove key (2, ff:ff:ff:ff:ff:ff) from hardware (-22)
[ 5883.308073] bridge-wlp2s0: disabling the bridge on dev down
[ 5883.308101] bridge-wlp2s0: down
[ 5883.308107] bridge-wlp2s0: detached
[ 5883.507422] userif-3: sent link down event.
[ 5883.507425] userif-3: sent link up event.
[ 5884.643364] PM: Syncing filesystems ... done.
[ 5884.649669] PM: Preparing system for sleep (mem)
[ 5884.652071] Freezing user space processes ... (elapsed 0.001 seconds) done.
[ 5884.654022] OOM killer disabled.
[ 5884.654022] Freezing remaining freezable tasks ... (elapsed 0.000 seconds) done.
[ 5884.654843] PM: Suspending system (mem)
[ 5884.654880] Suspending console(s) (use no_console_suspend to debug)
[ 5884.871980] sd 2:0:0:0: [sdb] Synchronizing SCSI cache
[ 5884.872111] sd 2:0:0:0: [sdb] Stopping disk
[ 5884.872195] sd 0:0:0:0: [sda] Synchronizing SCSI cache
[ 5884.874473] sd 0:0:0:0: [sda] Stopping disk
[ 5886.157004] PM: suspend of devices complete after 1285.783 msecs
[ 5886.174739] PM: late suspend of devices complete after 17.712 msecs
[ 5886.214758] PM: noirq suspend of devices complete after 40.018 msecs
[ 5886.215106] ACPI: Preparing to enter system sleep state S3
[ 5886.225502] ACPI: EC: event blocked
[ 5886.225503] ACPI: EC: EC stopped
[ 5886.225503] PM: Saving platform NVS memory
[ 5886.225606] Disabling non-boot CPUs ...
[ 5886.247167] IRQ 128: no longer affine to CPU1
[ 5886.248184] smpboot: CPU 1 is now offline
[ 5886.267540] IRQ 123: no longer affine to CPU2
[ 5886.267550] IRQ 124: no longer affine to CPU2
[ 5886.267559] IRQ 125: no longer affine to CPU2
[ 5886.269988] smpboot: CPU 2 is now offline
[ 5886.291443] IRQ 1: no longer affine to CPU3
[ 5886.291454] IRQ 8: no longer affine to CPU3
[ 5886.291463] IRQ 9: no longer affine to CPU3
[ 5886.291474] IRQ 16: no longer affine to CPU3
[ 5886.291485] IRQ 17: no longer affine to CPU3
[ 5886.291496] IRQ 109: no longer affine to CPU3
[ 5886.292573] smpboot: CPU 3 is now offline
[ 5886.297070] ACPI: Low-level resume complete
[ 5886.297190] ACPI: EC: EC started
[ 5886.297191] PM: Restoring platform NVS memory
[ 5886.298020] Suspended for 6102.426 seconds
[ 5886.298095] Enabling non-boot CPUs ...
[ 5886.298139] x86: Booting SMP configuration:
[ 5886.298140] smpboot: Booting Node 0 Processor 1 APIC 0x2
[ 5886.298713]  cache: parent cpu1 should not be sleeping
[ 5886.298885] CPU1 is up
[ 5886.298908] smpboot: Booting Node 0 Processor 2 APIC 0x1
[ 5886.299477]  cache: parent cpu2 should not be sleeping
[ 5886.299660] CPU2 is up
[ 5886.299685] smpboot: Booting Node 0 Processor 3 APIC 0x3
[ 5886.300188]  cache: parent cpu3 should not be sleeping
[ 5886.300422] CPU3 is up
[ 5886.304301] ACPI: Waking up from system sleep state S3
[ 5886.361549] PM: noirq resume of devices complete after 41.627 msecs
[ 5886.373120] PM: early resume of devices complete after 11.524 msecs
[ 5886.373330] ACPI: EC: event unblocked
[ 5886.373446] usb usb1: root hub lost power or was reset
[ 5886.373450] usb usb2: root hub lost power or was reset
[ 5886.373971] sd 0:0:0:0: [sda] Starting disk
[ 5886.373974] sd 2:0:0:0: [sdb] Starting disk
[ 5886.374613] iwlwifi 0000:02:00.0: RF_KILL bit toggled to enable radio.
[ 5886.384282] ACPI: button: The lid device is not compliant to SW_LID.
[ 5886.384481] rtc_cmos 00:01: Alarms can be up to one month in the future
[ 5886.687687] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[ 5886.687899] ata3: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[ 5886.688095] ata1.00: supports DRM functions and may not be fully accessible
[ 5886.689196] ata1.00: disabling queued TRIM support
[ 5886.691604] ata1.00: supports DRM functions and may not be fully accessible
[ 5886.692340] ata1.00: disabling queued TRIM support
[ 5886.694174] ata1.00: configured for UDMA/133
[ 5886.697127] ata3.00: configured for UDMA/133
[ 5886.723694] usb 1-6: reset high-speed USB device number 2 using xhci_hcd
[ 5886.783585] /dev/vmmon[0]: HostIFReadUptimeWork: detected settimeofday: fixed uptimeBase old 18445224561602123209 new 18445224555499697001 attempts 1
[ 5886.983901] usb 1-8: reset full-speed USB device number 3 using xhci_hcd
[ 5887.143066] PM: resume of devices complete after 769.948 msecs
[ 5887.143181] usb 1-8:1.0: rebind failed: -517
[ 5887.143186] usb 1-8:1.1: rebind failed: -517
[ 5887.145449] PM: Finishing wakeup.
[ 5887.145451] OOM killer enabled.
[ 5887.145452] Restarting tasks ... done.
[ 5887.160920] thermal thermal_zone9: failed to read out thermal zone (-5)
[ 5887.175561] Bluetooth: hci0: read Intel version: 370810011003110e00
[ 5887.175564] Bluetooth: hci0: Intel Bluetooth firmware file: intel/ibt-hw-37.8.10-fw-1.10.3.11.e.bseq
[ 5887.209791] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[ 5887.262954] [drm] RC6 on
[ 5887.320035] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[ 5887.376178] IPv6: ADDRCONF(NETDEV_UP): wlp2s0: link is not ready
[ 5887.483576] Bluetooth: hci0: Intel Bluetooth firmware patch completed and activated
[ 5891.547772] wlp2s0: authenticate with 88:ad:43:b9:2d:a8
[ 5891.557602] wlp2s0: send auth to 88:ad:43:b9:2d:a8 (try 1/3)
[ 5891.562644] wlp2s0: authenticated
[ 5891.567537] wlp2s0: associate with 88:ad:43:b9:2d:a8 (try 1/3)
[ 5891.581208] wlp2s0: RX AssocResp from 88:ad:43:b9:2d:a8 (capab=0x411 status=0 aid=1)
[ 5891.595382] wlp2s0: associated
[ 5891.595553] wlp2s0: Limiting TX power to 14 (17 - 3) dBm as advertised by 88:ad:43:b9:2d:a8
[ 5891.596346] IPv6: ADDRCONF(NETDEV_CHANGE): wlp2s0: link becomes ready
[ 5891.618368] /dev/vmnet: open called by PID 3260 (vmnet-bridge)
[ 5891.618382] /dev/vmnet: hub 0 does not exist, allocating memory.
[ 5891.618446] /dev/vmnet: port on hub 0 successfully opened
[ 5891.618465] bridge-wlp2s0: device is wireless, enabling SMAC
[ 5891.618469] bridge-wlp2s0: up
[ 5891.618784] bridge-wlp2s0: attached
[ 5891.818224] userif-3: sent link down event.
[ 5891.818225] userif-3: sent link up event.
[ 5895.394011] userif-3: sent link down event.
[ 5895.394019] userif-3: sent link up event.
"""


	newMessage = TextScroll(text_var_1)

	newMessage.marquee()

if __name__ == '__main__':
	main() 
