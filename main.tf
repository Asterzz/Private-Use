provider "oci" {}

resource "oci_core_instance" "generated_oci_core_instance" {
	agent_config {
		is_management_disabled = "false"
		is_monitoring_disabled = "false"
		plugins_config {
			desired_state = "DISABLED"
			name = "Vulnerability Scanning"
		}
		plugins_config {
			desired_state = "ENABLED"
			name = "Compute Instance Monitoring"
		}
		plugins_config {
			desired_state = "DISABLED"
			name = "Bastion"
		}
	}
	availability_config {
		recovery_action = "RESTORE_INSTANCE"
	}
	availability_domain = "ZUkK:AP-SINGAPORE-1-AD-1"
	compartment_id = "ocid1.tenancy.oc1..aaaaaaaais34d2tovvoqjh6bjxd47rs2tlzpmik5hxpfvpohafofbrslyrsq"
	create_vnic_details {
		assign_private_dns_record = "true"
		assign_public_ip = "true"
		subnet_id = "ocid1.subnet.oc1.ap-singapore-1.aaaaaaaa6pt4itgq76glagyueihkpkh3xqu54eqsbjd7saocfhxyy3uecnja"
	}
	display_name = "instance-20230305-2031"
	instance_options {
		are_legacy_imds_endpoints_disabled = "false"
	}
	is_pv_encryption_in_transit_enabled = "true"
	metadata = {
		"ssh_authorized_keys" = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5IeJPn1zeYIgAPywN4Te/rn0Nw0qs8bHXoJ9RkCfFy7dkdGi8rxmTMK9gs7VLBiJ7a7rMKhEjfhWv7YR0nvwAskLyj7pRGYJDmWg/CAeWYqhCPy68fZh/PnsXvnwYydeRX7tBqNMsAd1Kd/qOacZl1LMV+oPZRF7xtWY0Yw7iP0WCCTFqOm2UepA4hqR1Ma1rmxKzieFyVOeq0tvPueVbClDLnhFpFPWOU0gKitnJSiVtfesAqkO6jds+C0efB5oSwa/fr9smjzCFm9teRxCHcLKk9R+LbtQCwLJJgU9kSIbd8TenlOoO2/1Q3sAzW+B+/i4oDt0FU7q4VOXrnSWT ssh-key-2023-03-05"
	}
	shape = "VM.Standard.A1.Flex"
	shape_config {
		memory_in_gbs = "24"
		ocpus = "4"
	}
	source_details {
		boot_volume_size_in_gbs = "100"
		boot_volume_vpus_per_gb = "10"
		source_id = "ocid1.image.oc1.ap-singapore-1.aaaaaaaapgcl7ndb6epgmhbv2robcgmqlx2vnw5y7kjeejkt2fyioalzodjq"
		source_type = "image"
	}
}
