<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="title">Title</label>
                <input
                    type="text"
                    class="form-control"
                    id="title"
                    v-model="shipment.title"
                    v-validate="'required'"
                    name="title"
                    placeholder="Enter title"
                >
            </div>

            <div class="form-group">
                <label for="description">Description</label>
                <input
                    type="text"
                    class="form-control"
                    id="description"
                    v-model="shipment.description"
                    v-validate="'required'"
                    name="description"
                    placeholder="Enter description"
                >
            </div>

            <div class="form-group">
                <label for="quantity">Quantity</label>
                <input
                    type="number"
                    class="form-control"
                    id="quantity"
                    v-model="shipment.quantity"
                    v-validate="'required'"
                    name="quantity"
                    placeholder="Enter quantity"
                >
            </div>

            <div class="form-group">
              <label for="company">Company</label>
              <select
                name="company"
                class="form-control"
                v-validate="'required'"
                id="company"
                v-model="shipment.company"
              >
              <option v-for="item in options" :value="item.id" :key="item.id">{{ item.name }}</option>
              </select>
            </div>

            <div class="form-group">
                <label for="delivery_country">Delivery Country</label>
                <select
                    name="delivery_country"
                    class="form-control"
                    v-validate="'required'"
                    id="delivery_country"
                    v-model="shipment.delivery_country"
                >
                    <option value="BY">Belarus</option>
                    <option value="PL">Poland</option>
                    <option value="LT">Lithuania</option>
                    <option value="LV" disabled>Latvia</option>
                </select>
            </div>

            <div class="form-group">
                <label for="availability">Availability</label>
                <select
                    name="availability"
                    class="form-control"
                    v-validate="'required'"
                    id="availability"
                    v-model="shipment.availability"
                >
                    <option value="AVAILABLE">Available</option>
                    <option value="NOT AVAILABLE">Not available</option>
                </select>
            </div>

            <div class="form-group">
                <label for="delivery_status">Delivery Status</label>
                <select
                    name="delivery_status"
                    class="form-control"
                    v-validate="'required'"
                    id="delivery_status"
                    v-model="shipment.delivery_status"
                >
                    <option value="CREATED">Created</option>
                    <option value="RECEIVED">Information received</option>
                    <option value="IN QUEUE">In queue</option>
                    <option value="IN TRANSIT">In transit</option>
                    <option value="PICKUP">Available for pickup</option>
                    <option value="DELIVERED">Delivered</option>
                    <option value="CANCELED">Canceled</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Create</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            shipment: {
                title: '',
                description: '',
                quantity: 0,
                company: '',
                delivery_country: '',
                availability: '',
                delivery_status: ''
            },
            submitted: false,
            options: [],
            selectedOption: null,
        }
    },
    mounted() {
        this.loadOptions();
    },
    methods: {
        loadOptions: function () {
            axios.get('http://127.0.0.1:8000/api/companies/')
                .then( options => {
                    this.options = options.data;
                });
        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .post('http://127.0.0.1:8000/api/shipments/',
                        this.shipment
                    )
                    .then(response => {
                        this.$router.push('/shipments');
                    })
            });
        }
    },
}
</script>