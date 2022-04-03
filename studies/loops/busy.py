#!/usr/bin/env python
import time, os, sys


def slowPrint():

	printString = """00:00.0 Host bridge: Intel Corporation Sky Lake Host Bridge/DRAM Registers (rev 08)
	Subsystem: ASUSTeK Computer Inc. Skylake Host Bridge/DRAM Registers
	Flags: bus master, fast devsel, latency 0
	Capabilities: <access denied>
	Kernel driver in use: skl_uncore

00:02.0 VGA compatible controller: Intel Corporation Sky Lake Integrated Graphics (rev 07) (prog-if 00 [VGA controller])
	Subsystem: ASUSTeK Computer Inc. Skylake Integrated Graphics
	Flags: bus master, fast devsel, latency 0, IRQ 126
	Memory at de000000 (64-bit, non-prefetchable) [size=16M]
	Memory at c0000000 (64-bit, prefetchable) [size=256M]
	I/O ports at f000 [size=64]
	[virtual] Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: i915
	Kernel modules: i915

00:04.0 Signal processing controller: Intel Corporation Skylake Processor Thermal Subsystem (rev 08)
	Subsystem: ASUSTeK Computer Inc. Skylake Processor Thermal Subsystem
	Flags: bus master, fast devsel, latency 0, IRQ 16
	Memory at dfb20000 (64-bit, non-prefetchable) [size=32K]
	Capabilities: <access denied>
	Kernel driver in use: proc_thermal
	Kernel modules: processor_thermal_device

00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21) (prog-if 30 [XHCI])
	Subsystem: ASUSTeK Computer Inc. Sunrise Point-LP USB 3.0 xHCI Controller
	Flags: bus master, medium devsel, latency 0, IRQ 124
	Memory at dfb10000 (64-bit, non-prefetchable) [size=64K]
	Capabilities: <access denied>
	Kernel driver in use: xhci_hcd

00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
	Subsystem: ASUSTeK Computer Inc. Sunrise Point-LP Thermal subsystem
	Flags: bus master, fast devsel, latency 0, IRQ 18
	Memory at dfb38000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel_pch_thermal
	Kernel modules: intel_pch_thermal

00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller (rev 21)
	Subsystem: ASUSTeK Computer Inc. Sunrise Point-LP Serial IO I2C Controller
	Flags: bus master, fast devsel, latency 0, IRQ 16
	Memory at dfb37000 (64-bit, non-prefetchable) [size=4K]
	Capabilities: <access denied>
	Kernel driver in use: intel-lpss
	Kernel modules: intel_lpss_pci

00:15.1 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller (rev 21)
	Subsystem: ASUSTeK Computer Inc. Sunrise Point-LP Serial IO I2C Controller"""

	stringLength = len(printString)

	while True:
		for index, character in enumerate(printString):
			if index == (stringLength - 1):
				print(character)
				time.sleep(.001)
			else:
				print(character, sep='', end='', flush=True)
				time.sleep(.001)
	

def main():
	
	slowPrint()

if __name__ == '__main__':
	main()
