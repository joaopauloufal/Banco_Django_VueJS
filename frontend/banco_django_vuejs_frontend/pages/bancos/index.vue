<template>
  <section class="section">
    <b-table :data="bancosList">
      <b-table-column label="Código do Banco" field="codigo_banco" v-slot="props">
        {{ props.row.codigo_banco }}
      </b-table-column>
      <b-table-column label="Nome" field="codigo_banco" v-slot="props">
        {{ props.row.nome }}
      </b-table-column>
      <b-table-column label="Ações">
        -
      </b-table-column>
      <template #empty>
        <div class="has-text-centered">Não há bancos cadastrados.</div>
      </template>
    </b-table>
  </section>
</template>

<script lang="ts">

import { Vue, Component } from 'vue-property-decorator'
import { bancos } from '~/store'
import Banco from '~/types/Banco'

@Component
export default class BancosIndex extends Vue {

  created ():void {
    bancos.getBancos()
  }

  get bancosList ():Banco[] {
    return bancos.bancosList
  }

}

</script>
